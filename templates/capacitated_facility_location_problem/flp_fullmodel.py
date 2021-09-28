from gurobipy import Model, GRB
from flp_problem import FacilityLocationProblem

class FullModel:

    def __init__(self, flp:FacilityLocationProblem):
        self.flp = flp
        self.m = Model()

        # Creates the variables
        self.y = self.m.addVars(flp.n_facilities, flp.n_customers, name="y")
        self.x = self.m.addVars(flp.n_facilities, vtype=GRB.BINARY, name="x")

        # Creates the objective
        expr = 0
        for i in range(flp.n_facilities):
            expr += flp.fixed_costs[i] * self.x[i]
            for j in range(flp.n_customers):
                expr += flp.delivery_costs[i][j] * self.y[i, j]
        self.m.setObjective(expr, GRB.MINIMIZE)

        # Constraints
        for i in range(flp.n_facilities):
            self.m.addConstr(self.y.sum(i, '*') <= flp.capacity[i] * self.x[i])
        for j in range(flp.n_customers):
            self.m.addConstr(self.y.sum('*', j) >= flp.demands[j])

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        for i in range(self.flp.n_facilities):
            print('%s %g' % (self.x[i].varName, self.x[i].x))
        print('Obj: %g' % self.m.objVal)
