from gurobipy.gurobipy import Model, GRB
from solutions.facility_sizing.fsp_problem import FacilitySizingProblem

class FSP:

    def __init__(self, fsp:FacilitySizingProblem, x:list):
        self.fsp = fsp
        self.m = Model()

        # Creates the variables
        y = self.m.addVars(fsp.n_facilities, fsp.n_customers, name="y")
        v1 = self.m.addVars(fsp.n_facilities, name="v+")
        v2 = self.m.addVars(fsp.n_customers, name="v-")

        # Creates the objective
        expr = v1.sum() + v2.sum()
        self.m.setObjective(expr, GRB.MINIMIZE)

        # Constraints
        self.demand_c = self.m.addConstrs(y.sum('*', j) + v1[j] >= fsp.demands[j] for j in range(fsp.n_customers))
        self.capacity_c = self.m.addConstrs(y.sum(i, '*') - v2[i] <= x[i] for i in range(fsp.n_facilities))


    def solve(self):
        self.m.optimize()

    def getResults(self):
        '''
        Returns, in this order,
        1) the objective value,
        2) the vector of optimal duals for the capacity constraints
        3) the vector of optimal duals for the demand constraints
        :return:
        '''
        dualsCC = [self.capacity_c[i].Pi for i in range(self.fsp.n_facilities)]
        dualsDC = [self.demand_c[j].Pi for j in range(self.fsp.n_customers)]

        return self.m.objVal, dualsCC, dualsDC
