from solutions.uranium.uranium_problem import UraniumMineProblem
from gurobipy.gurobipy import Model, GRB, quicksum
class UraniumMineModel:

    """
    This class represents the model for the uranium mine problem.
    """

    def __init__(self,p: UraniumMineProblem):
        self.p = p
        self.m = Model('uranium')

        # Decision variables
        self.x = self.m.addVars(self.p.blocks,vtype=GRB.BINARY,name="x")
        # Objective function
        expr = quicksum([(p.values[b] - p.costs[b]) * self.x[b] for b in p.blocks])
        self.m.setObjective(expr,sense=GRB.MAXIMIZE)

        # Constraints
        self.m.addConstrs(self.x[a] - self.x[b] <= 0 for (a,b) in p.precedences)
        # Alternatively
        #self.m.addConstrs(self.x[a] - self.x[b] <= 0 for a, b in p.precedences)

    def solve(self):
        self.m.optimize()

    def printSolution(self):
        print("Total profit ", self.m.ObjVal)
        for b in self.p.blocks:
            print("%s %g"%(self.x[b].varName,self.x[b].x))