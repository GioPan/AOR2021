from gurobipy import Model, GRB, quicksum
from fsp_problem import FacilitySizingProblem

class FullModel:

    def __init__(self, fsp:FacilitySizingProblem):
        self.fsp = fsp
        self.m = Model()

        # Creates the variables
        self.y = self.m.addVars(fsp.n_facilities, fsp.n_customers, name="y")
        self.x = self.m.addVars(fsp.n_facilities, name="x")

        # Creates the objective
        # There are different ways of creating the objective function.
        # The first way is the following (easy to understand, but inefficient on the large scale):
        #expr = 0
        #for i in range(fsp.n_facilities):
        #    expr += fsp.fixed_costs[i] * self.x[i]
        #    for j in range(fsp.n_customers):
        #        expr += fsp.delivery_costs[i][j] * self.y[i, j]
        #self.m.setObjective(expr, GRB.MINIMIZE)

        # The second way is to create the two terms separately, using Gurobi's specific
        # features, such as prod and quicksum.
        # The first term can be created in at least two ways:
        #term1 = quicksum([fsp.fixed_costs[i] * self.x[i] for i in range(fsp.n_facilities)])
        # or, alteratively
        term1 = self.x.prod(fsp.fixed_costs)
        # The second way is preferable as it allows us to avoid generating the list to pass to quicksum

        # For the second term we need to use quicksum. There are possibly even better ways to do this.
        # For example, one could try to use the prod method of the y variables. But this would entail changing the
        # way we store delivery costs. Can you think of such a way?
        term2 = quicksum([fsp.delivery_costs[i][j] * self.y[i, j] for i in range(fsp.n_facilities) for j in range(fsp.n_customers)])
        self.m.setObjective(term1+term2, GRB.MINIMIZE)

        # Constraints
        # Also for the constraints we potentially have alternative ways of writing the same thing.
        # For example, we could build each capacity constraint individually as
        #for i in range(fsp.n_facilities):
        #    self.m.addConstrs(self.y.sum(i, '*') <= self.x[i])
        # A better way of doing this is the following.
        self.m.addConstrs(self.y.sum(i, '*') <= self.x[i] for i in range(fsp.n_facilities))
        # Notice that we are use the method sum of variable y since y is a tupledict
        self.m.addConstrs(self.y.sum('*', j) >= fsp.demands[j] for j in range(fsp.n_customers))
        self.m.addConstrs(self.x[i] <= self.fsp.capacity[i] for i in range(fsp.n_facilities))

    def solve(self):
        self.m.optimize()

    def print_solution(self):
        for i in range(self.fsp.n_facilities):
            print('%s %g' % (self.x[i].varName, self.x[i].x))
        print('Obj: %g' % self.m.objVal)
