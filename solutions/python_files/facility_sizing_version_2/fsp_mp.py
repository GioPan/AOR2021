from gurobipy import Model,GRB, quicksum
from fsp_problem import FacilitySizingProblem

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
        '''
        Returns two thing:
        - the x solution (a list of values, one for each facility)
        - the phi solution (a scalar).
        Alternatively, one may create two methods, one that returns only x and one that returns only phi.
        '''
        return [self.x[i].x for i in range(self.fsp.n_facilities)], self.phi.x

    def add_feasibility_cut(self,dualsCC:list,dualsDC:list, dualsPC:list):
        '''
        Adds a feasibility cut given the duals of the feasibility subproblem (extreme rays of polyhedral cone V).
        Note that the dual variables corresponding to the percentage constraints do not show up in the cut as the
        corresponding right-hand-side coefficient is 0.
        '''
        self.m.addConstr(quicksum([dualsCC[i] * self.x[i] for i in range(self.fsp.n_facilities)])
                         <= - sum([dualsDC[j] * self.fsp.demands[j] for j in range(self.fsp.n_customers)]))

        print("Added feasibility cut")

    def add_optimality_cut(self,dualsCC:list,dualsDC:list, dualsPC:list):
        '''
        Adds an optimality cut given the duals of the optimality subproblem (extreme points of the dual of the optimality subproblem).
        Note that the dual variables corresponding to the percentage constraints do not show up in the cut as the
        corresponding right-hand-side coefficient is 0.
        '''
        self.m.addConstr(self.phi - quicksum([dualsCC[i] * self.x[i] for i in range(self.fsp.n_facilities)])
                         >= sum([dualsDC[j] * self.fsp.demands[j] for j in range(self.fsp.n_customers)]))
        print("Added optimality cut")

    def print_solution(self):
        for i in range(self.fsp.n_facilities):
            print('%s %g' % (self.x[i].varName, self.x[i].x))
        print('Obj: %g' % self.m.objVal)



