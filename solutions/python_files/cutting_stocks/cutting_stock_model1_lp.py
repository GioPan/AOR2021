from gurobipy import GRB, Model, quicksum
from cutting_stock_problem import CuttingStockProblem


class CuttingStockModel1LP:

    def __init__(self, p:CuttingStockProblem):
        self.p = p
        self.m = Model('CS1')

        # Decision variables
        n_large_rolls = self.p.get_max_number_of_large_rolls()
        n_small_roll_types = len(self.p.demand)
        print(n_large_rolls,n_small_roll_types)
        y = self.m.addVars([i for i in range(n_large_rolls)],lb = 0, ub=1,vtype=GRB.CONTINUOUS,name="y")
        z = self.m.addVars([j for j in range(n_small_roll_types)],[i for i in range(n_large_rolls)],lb= 0, ub= GRB.INFINITY, vtype=GRB.CONTINUOUS,name="x")

        # Objective function
        self.m.setObjective(y.sum('*'))

        # Constraints
        # Note that the argument passed to quicksum is a list, and the list is built using comprehension
        self.m.addConstrs(quicksum([self.p.width_small_rolls[i] * z[i,j] for i in range(n_small_roll_types)]) <= self.p.width_large_rolls * y[j] for j in range(n_large_rolls))
        self.m.addConstrs(z.sum(i,'*') >= self.p.demand[i] for i in range(n_small_roll_types))

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        print("Objective ", self.m.objVal)
        for v in self.m.getVars():
            print("%s %g" % (v.varName, v.x))