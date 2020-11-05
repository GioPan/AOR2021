from gurobipy.gurobipy import Model,GRB

class OSP:

    def __init__(self, x: float):

        self.m = Model()
        self.y1 = self.m.addVar(name = "y1")
        self.y2 = self.m.addVar(name = "y2")

        # Objective function
        self.m.setObjective(self.y1 + 3*self.y2, sense=GRB.MINIMIZE)

        # Constraints
        self.c1 = self.m.addConstr(2 * self.y1 + self.y2 == 1 - x)
        self.c2 = self.m.addConstr(-self.y1 + self.y2  == 2 - 4 * x)

    def solve(self):
        self.m.optimize()

    def get_results(self):
        return self.m.objVal, self.c1.Pi, self.c2.Pi

    def print_solution(self):
        print('%s %g' % (self.y1.varName, self.y1.x))
        print('%s %g' % (self.y2.varName, self.y2.x))
        print('Obj: %g' % self.m.objVal)

