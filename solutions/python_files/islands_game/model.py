from problem import IslandsGame
from gurobipy import Model, GRB, quicksum
class IslandsGameModel:

    def __init__(self,p:IslandsGame):
        self.p = p

        self.m = Model('IGM')

        # Decision variables
        self.x = self.m.addVars(self.p.N,self.p.N,vtype=GRB.BINARY,name="x")

        # Objective function
        self.m.setObjective(0, sense=GRB.MINIMIZE)

        # Constraints
        self.m.addConstrs(quicksum([self.x[i,j] for j in range(self.p.N)]) == 1 for i in range(self.p.N))
        self.m.addConstrs(quicksum([self.x[i, j] for i in range(self.p.N)]) == 1 for j in range(self.p.N))
        self.m.addConstrs(quicksum([self.x[i, j] for i in range(self.p.N) for j in range(self.p.N) if self.p.islands[i,j] == k]) == 1 for k in range(self.p.N))
        self.m.addConstrs(self.x[i,j] + self.x[i,j+1]+ self.x[i+1,j]+self.x[i+1,j+1] <= 1 for i in range(self.p.N-1) for j in range(self.p.N-1))

    def solve(self):
        self.m.optimize()

    def print(self):
        self.m.write('model.lp')

    def print_solution(self):
        for i in range(self.p.N):
            for j in range(self.p.N):
                print('%3d' % self.x[i,j].x,end="")
            print()
