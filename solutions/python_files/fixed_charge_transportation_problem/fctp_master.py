from gurobipy import Model,GRB,quicksum
from fctp_problem import FixedChargeTransportationProblem
from fctp_fsp import FSP
from fctp_osp import OSP

class Master:
    def __init__(self, p:FixedChargeTransportationProblem):
        self.m = Model()
        self.p = p

        # Decision variables
        self.y = self.m.addVars(self.p.n_sources, self.p.n_sinks,vtype=GRB.BINARY, name="x")
        self.phi = self.m.addVar(name="phi")
        # Objective function
        self.m.setObjective(self.y.prod(self.p.fixed_charge)+self.phi,sense=GRB.MINIMIZE)

        # Makes the variables visible in the callback
        self.m._y = self.y
        self.m._phi = self.phi

    def solve(self):
        def callback(model, where):
            if where == GRB.Callback.MIPSOL:
                y_val = model.cbGetSolution(model._y)
                phi_val = model.cbGetSolution(model._phi)

                # Solves a FSP
                fsp = FSP(self.p, y_val)
                fsp.solve()
                obj = fsp.get_objective()
                duals_a, duals_b, duals_c = fsp.get_duals()
                print("Objective fsp ",obj)
                if obj > 0:
                    lhs = quicksum([self.p.supply[i] * duals_a[i] for i in range(self.p.n_sources)])
                    lhs = lhs + quicksum([self.p.demand[j] * duals_b[j] for j in range(self.p.n_sinks)])
                    lhs = lhs + quicksum([self.p.get_max_flow(i,j) * duals_c[i,j] * model._y[i,j] for i in range(self.p.n_sources) for j in range(self.p.n_sinks)])
                    model.cbLazy(lhs <= 0)
                    print("Added an FC")
                else:
                    # Solves an OSP
                    osp = OSP(self.p, y_val)
                    osp.solve()

                    obj = osp.get_objective()
                    duals_a, duals_b, duals_c = osp.get_duals()
                    if phi_val >= obj:
                        print("Optimal solution found")
                    else:
                        lhs = model._phi
                        rhs = quicksum([self.p.supply[i] * duals_a[i] for i in range(self.p.n_sources)])
                        rhs = rhs + quicksum([self.p.demand[j] * duals_b[j] for j in range(self.p.n_sinks)])
                        rhs = rhs + quicksum([self.p.get_max_flow(i, j) * duals_c[i, j] * model._y[i, j]
                                             for i in range(self.p.n_sources)
                                             for j in range(self.p.n_sinks)
                                             ])
                        model.cbLazy(lhs >= rhs)
                        print("Added an OC")

        # self.m.setParam(GRB.Param.DisplayInterval, 20)
        self.m.setParam(GRB.Param.LazyConstraints, 1)
        self.m.optimize(callback)

    def print_solution(self):
        print("Optimal objective value",self.m.objVal)
        print(self.m.getAttr('x', self.y))