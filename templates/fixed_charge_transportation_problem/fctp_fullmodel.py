from gurobipy import Model,GRB,quicksum
from fctp_problem import FixedChargeTransportationProblem

class FullModel:
    def __init__(self, p:FixedChargeTransportationProblem):
        self.m = Model()
        self.p = p

        # Decision variables
        self.x = self.m.addVars(self.p.n_sources,self.p.n_sinks,name="x")
        self.y = self.m.addVars(self.p.n_sources, self.p.n_sinks,vtype=GRB.BINARY, name="x")

        # Objective function
        self.m.setObjective(self.x.prod(self.p.transport_cost) + self.y.prod(self.p.fixed_charge),sense=GRB.MINIMIZE)

        # Constraints
        self.m.addConstrs(self.x.sum(i,'*') == self.p.supply[i] for i in range(self.p.n_sources))
        self.m.addConstrs(self.x.sum('*',j) == self.p.demand[j] for j in range(self.p.n_sinks))
        self.m.addConstrs(self.x[i,j] <= self.p.get_max_flow(i,j)*self.y[i,j] for i in range(self.p.n_sources) for j in range(self.p.n_sinks))

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        print("Optimal objective value ",self.m.objVal)
        print(self.m.getAttr('x',self.x))
        print(self.m.getAttr('x', self.y))
