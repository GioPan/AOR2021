from gurobipy.gurobipy import Model, GRB,Column
from procurement_problem.procurement_problem import ProcurementProblem
class PPSP:

    def __init__(self,pp:ProcurementProblem,material:int,pi:float):
        """
        Creates an instance of the DW's subproblem
        for a given material and given pi, the dual
        variable value corresponding to the complicating constraints
        in the RMP.
        :param pp:
        :param product:
        :param pi:
        """

        self.pp = pp
        self.m = Model()
        self.material = material

        # The subproblem has only one decision variable
        self.x = self.m.addVar()

        # The objective function will be
        # (c_j - pi A_j)*x, where j = material
        expr = (self.pp.costs[material] - pi*self.pp.consumption[material]) * self.x
        self.m.setObjective(expr, GRB.MINIMIZE)

        # The constraints bind the value of x to a min and max production quantity
        self.m.addConstr(self.x <=  self.pp.max_production[material])
        self.m.addConstr(self.x >= self.pp.min_production[material])

    def solve(self):
        """
        Solves the subproblem.
        :return:
        """
        # By setting the OutputFlag to 0 we tell
        # Gurobi not to print details about the solution of the subproblem.
        # We do this in order to obtain a more readable output.
        self.m.setParam(GRB.Param.OutputFlag,0)
        self.m.optimize()

    def get_solution(self):
        """
        Retrieves the solution to the subproblem.
        :return:
        """
        return self.x.x

    def get_objective(self):
        """
        Retrieves the optimal objective value.
        :return:
        """
        return self.m.objVal


