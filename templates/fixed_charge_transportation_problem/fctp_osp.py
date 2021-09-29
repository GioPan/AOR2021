from gurobipy import Model,GRB,quicksum
from fctp_problem import FixedChargeTransportationProblem

class OSP:
    def __init__(self, p:FixedChargeTransportationProblem, y:dict):
        self.m = Model()
        self.p = p

        # Decision variables
        self.x = self.m.addVars(self.p.n_sources,self.p.n_sinks,name="x")

        # Objective function
        self.m.setObjective(self.x.prod(self.p.transport_cost),sense=GRB.MINIMIZE)

        # Constraints
        self.c1 = self.m.addConstrs(self.x.sum(i,'*') == self.p.supply[i] for i in range(self.p.n_sources))

        # TODO: CREATE THE REMAINING CONSTRAINTS

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        print(self.m.getAttr('x', self.x))

    def get_objective(self):
        return self.m.objVal

    def get_duals(self):
        print("TBD")
        # TODO: RETURN THE OPTIMAL DUAL SOLUTION