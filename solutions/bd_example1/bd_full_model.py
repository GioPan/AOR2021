from gurobipy.gurobipy import Model,GRB

class FullModel:

    def __init__(self):

        self.m = Model()
        self.x = self.m.addVar(name = "x")
        self.y1 = self.m.addVar(name = "y1")
        self.y2 = self.m.addVar(name = "y2")

        # Objective function
        self.m.setObjective(2 * self.x + self.y1 + 3*self.y2, sense=GRB.MINIMIZE)

        # Constraints
        self.m.addConstr(2 * self.y1 + self.y2 + self.x == 1)
        self.m.addConstr(-self.y1 + self.y2 + 4 * self.x == 2)

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        print('%s %g' % (self.x.varName, self.x.x))
        print('%s %g' % (self.y1.varName, self.y1.x))
        print('%s %g' % (self.y2.varName, self.y2.x))
        print('Obj: %g' % self.m.objVal)

