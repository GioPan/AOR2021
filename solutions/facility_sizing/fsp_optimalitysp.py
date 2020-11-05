from gurobipy.gurobipy import Model, GRB
from solutions.facility_sizing.fsp_problem import FacilitySizingProblem

class OSP:

    def __init__(self, fsp:FacilitySizingProblem, x:list):
        self.fsp = fsp
        self.m = Model()

        # Creates the variables
        y = self.m.addVars(fsp.n_facilities, fsp.n_customers, name="y")

        # Creates the objective
        expr = 0
        for i in range(fsp.n_facilities):
            for j in range(fsp.n_customers):
                expr += fsp.delivery_costs[i][j] * y[i, j]
        self.m.setObjective(expr, GRB.MINIMIZE)

        # Constraints
        self.capacity_constr = self.m.addConstrs(y.sum(i, '*') <= x[i] for i in range(self.fsp.n_facilities))
        self.demand_constr = self.m.addConstrs(y.sum('*', j) >= fsp.demands[j] for j in range(fsp.n_customers))

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
        print(self.capacity_constr)
        dualsCC = self.m.getAttr(GRB.Attr.Pi, self.capacity_constr)
        dualsDC = self.m.getAttr(GRB.Attr.Pi, self.demand_constr)

        return self.m.objVal, dualsCC, dualsDC
