from gurobipy import Model, GRB, quicksum
from fsp_problem import FacilitySizingProblem

class FullModel:

    def __init__(self, fsp:FacilitySizingProblem):
        self.fsp = fsp
        self.m = Model()

        # Creates the variables
        self.y = self.m.addVars(fsp.n_facilities, fsp.n_customers, name="y")
        self.x = self.m.addVars(fsp.n_facilities, name="x")

        term1 = self.x.prod(fsp.fixed_costs)
        term2 = quicksum([fsp.delivery_costs[i][j] * self.y[i, j] for i in range(fsp.n_facilities) for j in range(fsp.n_customers)])
        self.m.setObjective(term1+term2, GRB.MINIMIZE)

        # Constraints

        self.m.addConstrs(self.y.sum(i, '*') <= self.x[i] for i in range(fsp.n_facilities))
        self.m.addConstrs(self.y.sum('*', j) >= fsp.demands[j] for j in range(fsp.n_customers))
        self.m.addConstrs(self.x[i] <= self.fsp.capacity[i] for i in range(fsp.n_facilities))

        # At least 10% of the quantities delivered to each customer must come from a special location
        self.m.addConstrs(quicksum([self.y[i,j] for i in self.fsp.special_locations]) >= self.fsp.percentage_from_special_locations * self.y.sum('*',j) for j in range(self.fsp.n_customers))

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        for i in range(self.fsp.n_facilities):
            print('%s %g' % (self.x[i].varName, self.x[i].x))
        print('Obj: %g' % self.m.objVal)
