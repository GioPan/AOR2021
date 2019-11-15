from gurobipy import Model, GRB
from cflp.flp_fsp import FSP
from cflp.flp_osp import OSP


class Master:

    def __init__(self, flp):
        self.flp = flp
        self.m = Model()

        # Creates the variables
        x = self.m.addVars(flp.n_facilities, vtype=GRB.BINARY, name="x")
        phi = self.m.addVar(name="phi")

        # Makes the variables visible in the callback
        self.m._x = x
        self.m._phi = phi

        # Creates the objective
        expr = phi
        for i in range(flp.n_facilities):
            expr += flp.fixed_costs[i] * x[i]
        self.m.setObjective(expr, GRB.MINIMIZE)

    def solve(self):
        def callback(model, where):
            if where == GRB.Callback.MIPSOL:
                x_val = model.cbGetSolution(model._x)
                phi_val = model.cbGetSolution(model._phi)

                # Solves a FSP
                fsp = FSP(self.flp, x_val)
                fsp.solve()
                obj, dualsCC, dualsDC = fsp.getDuals()

                if obj > 0:
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

                    obj, dualsCC, dualsDC = osp.getResults()
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

        # self.m.setParam(GRB.Param.DisplayInterval, 20)
        self.m.setParam(GRB.Param.LazyConstraints, 1)
        self.m.optimize(callback)

    def print_solution(self):
        for i in range(self.flp.n_facilities):
            print('%s %g' % (self.m._x[i].varName, self.m._x[i].x))
        print('Obj: %g' % self.m.objVal)




