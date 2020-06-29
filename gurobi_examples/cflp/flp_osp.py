from gurobipy import Model, GRB


class OSP:

    def __init__(self, flp, x):
        self.flp = flp
        self.m = Model()

        # Creates the variables
        y = self.m.addVars(flp.n_facilities, flp.n_customers, name="y")

        # Creates the objective
        expr = 0
        for i in range(flp.n_facilities):
            for j in range(flp.n_customers):
                expr += flp.delivery_costs[i][j] * y[i, j]
        self.m.setObjective(expr, GRB.MINIMIZE)

        # Constraints
        self.dc = []
        self.cc = []
        for i in range(flp.n_facilities):
            self.cc.append(self.m.addConstr(y.sum(i, '*') <= flp.capacity[i] * x[i]))
        for j in range(flp.n_customers):
            self.dc.append(self.m.addConstr(y.sum('*', j) >= flp.demands[j]))

    def solve(self):
        self.m.optimize()

    def getResults(self):

        dualsCC = self.m.getAttr(GRB.Attr.Pi, self.cc)
        dualsDC = self.m.getAttr(GRB.Attr.Pi, self.dc)

        return self.m.objVal, dualsCC, dualsDC
