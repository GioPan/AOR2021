from alloy_problem import AlloyProductionProblem
from gurobipy import Model, GRB, quicksum
class AlloyProductionModel:
    """
    This class represents the mathematical model for the Alloy Production Problem.
    """
    def __init__(self,p:AlloyProductionProblem):
        self.p = p
        self.m = Model('APP')

        # Creates the decision variables
        self.materials = list(p.availability.keys())
        chemicals = list(p.max_grade.keys())
        self.x = self.m.addVars(self.materials,name='x')

        # Creates the objective function
        expr = self.x.prod(p.cost)
        self.m.setObjective(expr,sense= GRB.MINIMIZE)

        # Creates the constraints
        # Min content
        self.m.addConstrs(quicksum([p.content[(k,m)]* self.x[m] for m in self.materials]) >= p.min_grade[k] * self.x.sum('*') for k in chemicals)
        # Max content
        self.m.addConstrs(quicksum([p.content[(k, m)] * self.x[m] for m in self.materials]) <= p.max_grade[k] * self.x.sum('*') for k in chemicals)
        # Availability
        self.m.addConstrs(self.x[m] <= p.availability[m] for m in self.materials)
        # Demand
        self.m.addConstr(self.x.sum('*') >= p.demand)

    def solve(self):
        self.m.optimize()
        
    def print_solution(self):
        print("Objective ",self.m.ObjVal)
        for m in self.materials:
            print("%s %g "% (self.x[m].varName,self.x[m].x))

