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
        self.m.setObjective(self.q,sense=GRB.MINIMIZE)

        # Constraints
        self.m.addConstrs(self.q - self.x[t] >= 0 for t in p.tasks)
        self.m.addConstrs(self.x[t1] - self.x[t2] >= p.durations[t1] for (t1,t2) in p.precedences)
        self.m.addConstrs(self.x[t] >= p.durations[t] for t in p.tasks)

    def solve(self):
        self.m.optimize()

    def printSolution(self):
        print("Completion time ", self.m.ObjVal)
        for t in self.p.tasks:
            print("%s %g"%(self.x[t].varName,self.x[t].x))