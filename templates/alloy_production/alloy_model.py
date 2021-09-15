from alloy_production_problem import AlloyProductionProblem
from gurobipy import Model, GRB, quicksum
class AlloyProductionModel:
    """
    This class represents the mathematical model for the Alloy Production Problem.
    """
    def __init__(self,p:AlloyProductionProblem):
        self.p = p
        self.m = Model('APP')

        # TODO: Create the decision variables here
        
        # TODO: Create the objective function here
        
        # TODO: Create the constraints here
        
    def solve(self):
        self.m.optimize()
        
    def print_solution(self):
        print("Objective ",self.m.ObjVal)
        for m in self.materials:
            print("%s %g "% (self.x[m].varName,self.x[m].x))

