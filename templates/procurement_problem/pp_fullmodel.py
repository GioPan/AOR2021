from gurobipy import Model, GRB
from pp_problem import ProcurementProblem


class PPFullModel():
    """
    Class representing the full model for the procurement problem.
    """

    def __init__(self, pp: ProcurementProblem):
        self.m = Model()
        self.pp = pp

        # Creates the variables
        self.x = self.m.addVars(self.pp.n_materials, name="x")

        # Creates the objective
        # The expression is obtained by multiplying x to the costs dictionary.
        # See the Gurobi docs for tupledic product here
        # https://www.gurobi.com/documentation/8.1/refman/py_tupledict_prod.html
        expr = self.x.prod(self.pp.costs)
        self.m.setObjective(expr, GRB.MINIMIZE)

        # Creates the constraints
        self.m.addConstrs((self.x[i] <= self.pp.max_production[i] for i in range(self.pp.n_materials)), name='max_p')
        self.m.addConstrs((self.x[i] >= self.pp.min_production[i] for i in range(self.pp.n_materials)), name='min_p')
        self.m.addConstr(self.x.prod(self.pp.consumption) >= self.pp.demand)

    def solve(self):
        """
        Solves the problem.
        :return:
        """
        self.m.optimize()

    def print_solution(self):
        """
        Prints the solution to the problem.
        :return:
        """
        for i in range(self.pp.n_materials):
            print('%s %g' % (self.x[i].varName, self.x[i].x))
        print('Obj: %g' % self.m.objVal)
