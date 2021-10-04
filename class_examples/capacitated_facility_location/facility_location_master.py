from gurobipy.gurobipy import Model, GRB

from facility_location_problem import FacilityLocationProblem
from facility_location_fsp import FSP
from facility_location_osp import OSP


class Master:

    def __init__(self, flp:FacilityLocationProblem):
        self.flp = flp
        self.m = Model()

        # Creates the variables
        self.x = self.m.addVars(flp.n_facilities, vtype=GRB.BINARY, name="x")
        self.phi = self.m.addVar(name="phi")

        # Makes the variables visible in the callback
        self.m._x = self.x
        self.m._phi = self.phi

        # Creates the objective
        expr = self.phi
        for i in range(flp.n_facilities):
            expr += flp.fixed_costs[i] * self.x[i]
        self.m.setObjective(expr, GRB.MINIMIZE)

    def solve(self):

        def callback(model, where):
            # We want to run our callback ONLY
            # upon reaching a node in the Branch and Bound tree
            # with an integer solution. Gurobi calls this
            # condition GRB.Callback.MIPSOL.
            # Every time Gurobi calls our callback, it passes a value to the "where"
            # argument. Thus our callback code must run only when where indicates
            # that we are at an integer node (i.e., where is equal to GRB.Callback.MIPSOL).
            if where == GRB.Callback.MIPSOL:
                # Note that here we need to get the value
                # of the solution AT THE INTEGER NODE we have arrived at.
                # Observe how this value is retrieved, and that it is different
                # from what we learnt before (self.m.getAttr('x',x) or self.x.x).
                x_val = model.cbGetSolution(model._x)
                phi_val = model.cbGetSolution(model._phi)

                # Solves a FSP
                fsp = FSP(self.flp, x_val)
                fsp.solve()
                obj, dualsCC, dualsDC = fsp.get_results()

                # Feasibility test
                if obj > 0:
                    # Can you write the cut in a better way?
                    lhs = 0
                    for i in range(self.flp.n_facilities):
                        lhs = lhs + dualsCC[i] * self.flp.capacity[i] * model._x[i]
                    for j in range(self.flp.n_customers):
                        lhs = lhs + dualsDC[j] * self.flp.demands[j]
                    model.cbLazy(lhs <= 0)
                    print("Added an FC")
                else:
                    # Solves an OSP
                    osp = OSP(self.flp, x_val)
                    osp.solve()

                    obj, dualsCC, dualsDC = osp.get_results()

                    # Optimality test
                    if phi_val >= obj:
                        print("Optimal solution found")
                    else:
                        lhs = model._phi
                        rhs = 0
                        for i in range(self.flp.n_facilities):
                            rhs = rhs + dualsCC[i] * self.flp.capacity[i] * model._x[i]
                        for j in range(self.flp.n_customers):
                            rhs = rhs + dualsDC[j] * self.flp.demands[j]
                        model.cbLazy(lhs >= rhs)
                        print("Added an OC")

        # We inform Gurobi that we are going to pass
        # Lazy Constraints.
        self.m.setParam(GRB.Param.LazyConstraints, 1)
        # We pass the callback to the optimize method.
        self.m.optimize(callback)

    def print_solution(self):
        for i in range(self.flp.n_facilities):
            print('%s %g' % (self.x[i].varName, self.x[i].x))
        print('Obj: %g' % self.m.objVal)




