from gurobipy import GRB, Model, quicksum
from cutting_stock_problem import CuttingStockProblem


class CuttingStockModel2LP:

    def __init__(self, p:CuttingStockProblem):
        self.p = p
        self.m = Model('CS1')

        # Decision variables
        n_patterns = len(self.p.get_feasible_patterns())

        x = self.m.addVars(n_patterns,lb= 0, ub= GRB.INFINITY, vtype=GRB.CONTINUOUS,name="x")

        # Objective function
        self.m.setObjective(x.sum('*'))

        # Constraints
        # Note that the argument passed to quicksum is a list, and the list is built using comprehension
        self.m.addConstrs(quicksum([self.p.get_feasible_patterns()[q][i] * x[q] for q in range(n_patterns)]) >= self.p.demand[i]  for i in range(len(p.demand)))

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        print("Objective ", self.m.objVal)
        for v in self.m.getVars():
            print("%s %g" % (v.varName, v.x))