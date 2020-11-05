from gurobipy.gurobipy import Model,GRB, quicksum
from solutions.facility_sizing.fsp_problem import FacilitySizingProblem

class Master:

    def __init__(self, fsp:FacilitySizingProblem):
        self.fsp = fsp
        self.m = Model()

        # Creates the variables
        self.x = self.m.addVars(fsp.n_facilities, vtype=GRB.CONTINUOUS, name="x")
        self.phi = self.m.addVar(name="phi")

        # Creates the objective
        expr = self.phi + quicksum([self.fsp.fixed_costs[i] * self.x[i] for i in range(self.fsp.n_facilities)])
        self.m.setObjective(expr, GRB.MINIMIZE)

        # Creates the constraints
        self.m.addConstrs(self.x[i] <= self.fsp.capacity[i] for i in range(fsp.n_facilities))

    def solve(self):
        self.m.optimize()

    def get_solution(self):
        return [self.x[i].x for i in range(self.fsp.n_facilities)], self.phi.x

    def add_feasibility_cut(self,dualsCC:list,dualsDC:list):
        self.m.addConstr(quicksum([dualsCC[i] * self.x[i] for i in range(self.fsp.n_facilities)])
                         <= - sum([dualsDC[j] * self.fsp.demands[j] for j in range(self.fsp.n_customers)]))
        print("Added feasibility cut")

    def add_optimality_cut(self,dualsCC:list,dualsDC:list):
        self.m.addConstr(self.phi - quicksum([dualsCC[i] * self.x[i] for i in range(self.fsp.n_facilities)])
                         >= sum([dualsDC[j] * self.fsp.demands[j] for j in range(self.fsp.n_customers)]))
        print("Added optimality cut")

    def print_solution(self):
        for i in range(self.fsp.n_facilities):
            print('%s %g' % (self.x[i].varName, self.x[i].x))
        print('Obj: %g' % self.m.objVal)



