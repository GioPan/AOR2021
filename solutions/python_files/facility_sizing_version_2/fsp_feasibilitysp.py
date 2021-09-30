from gurobipy import Model, GRB, quicksum
from fsp_problem import FacilitySizingProblem

class FSP:

    def __init__(self, fsp:FacilitySizingProblem, x:list):
        self.fsp = fsp
        self.m = Model()

        # Creates the variables
        y = self.m.addVars(fsp.n_facilities, fsp.n_customers, name="y")
        v1 = self.m.addVars(fsp.n_facilities, name="v1")
        v2 = self.m.addVars(fsp.n_customers, name="v2")
        v3 = self.m.addVars(fsp.n_customers, name="v3")

        # Creates the objective
        expr = v1.sum() + v2.sum() + v3.sum()
        self.m.setObjective(expr, GRB.MINIMIZE)

        # Constraints
        self.demand_c = self.m.addConstrs(y.sum('*', j) + v1[j] >= fsp.demands[j] for j in range(fsp.n_customers))
        self.capacity_c = self.m.addConstrs(y.sum(i, '*') - v2[i] <= x[i] for i in range(fsp.n_facilities))
        self.percentage_c = self.m.addConstrs(quicksum([y[i, j] for i in  self.fsp.special_locations]) - self.fsp.percentage_from_special_locations * y.sum('*', j) + v3[j] >= 0  for j in range(self.fsp.n_customers))

    def solve(self):
        self.m.optimize()

    def getResults(self):
        '''
        Returns, in this order,
        1) the objective value,
        2) the vector of optimal duals for the capacity constraints
        3) the vector of optimal duals for the demand constraints
        4) the vector of optimal dual for the percentage constraints
        Alternatively, one may create three methods, one for the objective value, one for the duals of the capacity constraints
        and one for the duals of the demand constraints.
        '''
        dualsCC = [self.capacity_c[i].Pi for i in range(self.fsp.n_facilities)]
        dualsDC = [self.demand_c[j].Pi for j in range(self.fsp.n_customers)]
        dualsPC = [self.percentage_c[j].Pi for j in range(self.fsp.n_customers)]

        return self.m.objVal, dualsCC, dualsDC, dualsPC
