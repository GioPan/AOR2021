from gurobipy import Model, GRB, quicksum

from stadium_problem import StadiumConstructionProblem


class StadiumConstructionModel:

    """
    This class represents the model for the Stadium Construction problem.
    """

    def __init__(self,p: StadiumConstructionProblem):
        self.p = p
        self.m = Model('stadium')

        # Decision variables
        self.x = self.m.addVars(self.p.tasks,name="x")
        self.q = self.m.addVar(name = "maxtime")

        # Objective function
        # TODO: Write the objective function here

        # Constraints
        # TODO: Write the constraints here

    def solve(self):
	# TODO: solve the model here

    def printSolution(self):
	# TODO: print the solution here
