from gurobipy.gurobipy import Model,GRB

class FSP:

    def __init__(self,x):

        self.m = Model()
        self.y1 = self.m.addVar(name = "y1")
        self.y2 = self.m.addVar(name = "y2")
        self.v1 = self.m.addVar(name="v1")
        self.v2 = self.m.addVar(name="v2")
        self.v3 = self.m.addVar(name="v3")
        self.v4 = self.m.addVar(name="v4")

        # Objective function
        self.m.setObjective( self.v1 + self.v2+ self.v3 + self.v4, sense=GRB.MINIMIZE)

        # Constraints
        self.c1 = self.m.addConstr(2 * self.y1 + self.y2 + self.v1 - self.v2 == (1 - x))
        self.c2 = self.m.addConstr(-self.y1 + self.y2 + self.v3 - self.v4 == (2 - 4 * x))

    def solve(self):
        self.m.optimize()

    def get_results(self):
        print(self.m.objVal, self.c1.Pi, self.c2.Pi)
        return self.m.objVal, self.c1.Pi, self.c2.Pi

    def print_solution(self):
        print('%s %g' % (self.y1.varName, self.y1.x))
        print('%s %g' % (self.y2.varName, self.y2.x))
        print('%s %g' % (self.v1.varName, self.v1.x))
        print('%s %g' % (self.v2.varName, self.v2.x))
        print('%s %g' % (self.v3.varName, self.v3.x))
        print('%s %g' % (self.v4.varName, self.v4.x))
        print('Obj: %g' % self.m.objVal)

