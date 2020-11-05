from gurobipy.gurobipy import Model, GRB
from solutions.facility_sizing.fsp_problem import FacilitySizingProblem

class FullModel:

    def __init__(self, fsp:FacilitySizingProblem):
        self.fsp = fsp
        self.m = Model()

        # Creates the variables
        self.y = self.m.addVars(fsp.n_facilities, fsp.n_customers, name="y")
        self.x = self.m.addVars(fsp.n_facilities, name="x")

        # Creates the objective
        expr = 0
        for i in range(fsp.n_facilities):
            expr += fsp.fixed_costs[i] * self.x[i]
            for j in range(fsp.n_customers):
                expr += fsp.delivery_costs[i][j] * self.y[i, j]
        self.m.setObjective(expr, GRB.MINIMIZE)

        # Constraints
        for i in range(fsp.n_facilities):
            self.m.addConstr(self.y.sum(i, '*') <= self.x[i])
        for j in range(fsp.n_customers):
            self.m.addConstr(self.y.sum('*', j) >= fsp.demands[j])

        self.m.addConstrs(self.x[i] <= self.fsp.capacity[i] for i in range(fsp.n_facilities))

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        for i in range(self.fsp.n_facilities):
            print('%s %g' % (self.x[i].varName, self.x[i].x))
        print('Obj: %g' % self.m.objVal)
