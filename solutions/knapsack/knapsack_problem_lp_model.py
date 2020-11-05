from gurobipy.gurobipy import Model, GRB, quicksum

from solutions.knapsack.knapsack_problem import KnapsackProblem
class KnapsackProblemLPModel:

    def __init__(self,p:KnapsackProblem):
        self.p = p
        self.m = Model('knapsack')
        # Creates the decision variables
        self.x = self.m.addVars(len(p.rewards),lb=0,ub=1,vtype = GRB.CONTINUOUS,name = "x")

        # Creates the objective
        self.m.setObjective(quicksum([self.p.rewards[i] * self.x[i] for i in range(len(self.p.rewards))]),sense=GRB.MAXIMIZE)

        # Creates the constraint
        self.m.addConstr(quicksum([self.p.weights[i] * self.x[i] for i in range(len(self.p.weights))]) <= self.p.capacity)

    def addCover(self,indices:list,rhs:int):
        self.m.addConstr(quicksum([self.x[indices[i]] for i in range(len(indices))]) <= rhs)

    def printModel(self):
        self.m.write('knapsack.lp')
    def solve(self):
        self.m.optimize()

    def printSolution(self):
        print("Objective ", self.m.objVal)
        for v in self.m.getVars():
            print('%s %g' % (v.varName, v.x))