from uranium_problem import UraniumMineProblem
from gurobipy import Model, GRB, quicksum

class UraniumMineModel:

    """
    This class represents the model for the uranium mine problem.
    """

    def __init__(self,p: UraniumMineProblem):
        # TODO: Write the optimization problem here

    def solve(self):
        self.m.optimize()

    def printSolution(self):
        print("Total profit ", self.m.ObjVal)
        for b in self.p.blocks:
            print("%s %g"%(self.x[b].varName,self.x[b].x))