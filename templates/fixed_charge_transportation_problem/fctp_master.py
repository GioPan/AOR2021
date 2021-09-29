from gurobipy import Model,GRB,quicksum
from fctp_problem import FixedChargeTransportationProblem
from fctp_fsp import FSP
from fctp_osp import OSP

class Master:
    def __init__(self, p:FixedChargeTransportationProblem):
        self.m = Model()
        self.p = p

        # Decision variables
        self.y = self.m.addVars(self.p.n_sources, self.p.n_sinks,vtype=GRB.BINARY, name="x")
        self.phi = self.m.addVar(name="phi")
        # Objective function
        self.m.setObjective(self.y.prod(self.p.fixed_charge)+self.phi,sense=GRB.MINIMIZE)

        # Makes the variables visible in the callback
        self.m._y = self.y
        self.m._phi = self.phi

    def solve(self):
        def callback(model, where):
            print("TBD")
            # TODO: COMPLETE THE CALLBACK TO ADD CUTS AT INTEGER NODES

        self.m.setParam(GRB.Param.LazyConstraints, 1)
        self.m.optimize(callback)

    def print_solution(self):
        print("Optimal objective value",self.m.objVal)
        print(self.m.getAttr('x', self.y))