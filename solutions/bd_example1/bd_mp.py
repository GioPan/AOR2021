from gurobipy.gurobipy import Model,GRB

class MP:

    def __init__(self):

        self.m = Model()
        self.x = self.m.addVar(name = "x")
        self.phi = self.m.addVar(name= "phi")

        # Objective function
        self.m.setObjective(2 * self.x + self.phi, sense=GRB.MINIMIZE)

        # Constraints

    def solve(self):
        self.m.optimize()

    def get_sol(self):
        return self.x.x, self.phi.x

    def add_feasibility_cuts(self,pi1:float,pi2:float):
        print(pi1,pi2)
        self.m.addConstr((pi1+(4*pi2))*self.x >= (pi1+(2*pi2)))

    def add_optimality_cuts(self, pi1: float, pi2: float):
        self.m.addConstr(self.phi + (pi1 + 4 * pi2) * self.x >= (pi1 + 2 * pi2))

    def print_solution(self):
        print('%s %g' % (self.x.varName, self.x.x))
        print('%s %g' % (self.phi.varName, self.phi.x))
        print('Obj: %g' % self.m.objVal)

    def write_model(self):
        self.m.write("mp.lp")

