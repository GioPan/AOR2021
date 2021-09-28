from gurobipy import Model, GRB
from flp_problem import FacilityLocationProblem

class OSP:

    def __init__(self, flp:FacilityLocationProblem, x:list):
        # TODO: Write the model of the optimality subproblem

    def solve(self):
        self.m.optimize()

    def getResults(self):

        dualsCC = self.m.getAttr(GRB.Attr.Pi, self.cc)
        dualsDC = self.m.getAttr(GRB.Attr.Pi, self.dc)

        return self.m.objVal, dualsCC, dualsDC
