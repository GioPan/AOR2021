from gurobipy import Model,GRB,quicksum
from fctp_problem import FixedChargeTransportationProblem

class FSP:
    def __init__(self, p:FixedChargeTransportationProblem, y:dict):
        self.m = Model()
        self.p = p

        # Decision variables
        self.x = self.m.addVars(self.p.n_sources,self.p.n_sinks,name="x")
        self.vA1 = self.m.addVars(self.p.n_sources,name="vA+")
        self.vA2 = self.m.addVars(self.p.n_sources, name="vA-")
        self.vB1 = self.m.addVars(self.p.n_sinks, name="vB+")
        self.vB2 = self.m.addVars(self.p.n_sinks, name="vB-")
        self.vC = self.m.addVars(self.p.n_sources,self.p.n_sinks,name="vC")
        # Objective function
        self.m.setObjective(self.vA1.sum()+self.vA2.sum()+self.vB1.sum()+self.vB2.sum() + self.vC.sum(),sense=GRB.MINIMIZE)

        # Constraints
        self.c1 = self.m.addConstrs(self.x.sum(i,'*') + self.vA1[i] - self.vA2[i] == self.p.supply[i] for i in range(self.p.n_sources))
        self.c2 = self.m.addConstrs(self.x.sum('*',j) + self.vB1[j] - self.vB2[j] == self.p.demand[j] for j in range(self.p.n_sinks))
        self.c3 = self.m.addConstrs(self.x[i,j] - self.vC[i,j] <= self.p.get_max_flow(i,j)*y[i,j] for i in range(self.p.n_sources) for j in range(self.p.n_sinks))

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        print(self.m.getAttr('x',self.x))


    def get_objective(self):
        return self.m.objVal

    def get_duals(self):
        return self.m.getAttr(GRB.Attr.Pi,self.c1), self.m.getAttr(GRB.Attr.Pi,self.c2), self.m.getAttr(GRB.Attr.Pi,self.c3)