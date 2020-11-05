from gurobipy.gurobipy import Model, GRB, Column
from solutions.procurement_problem.pp_subproblem import PPSP
from solutions.procurement_problem.pp_problem import ProcurementProblem


class RMP():

    def __init__(self, pp: ProcurementProblem):
        """
        Builds an instance of the DW's RMP for the
        Procurement Problem.
        :param pp:
        """

        # Builds an instance of the model
        self.m = Model()
        self.pp = pp
        # In the following list it will store all columns added to RMP during the DW algorithm
        self.columns = []

        # Initially there is no variable,
        # but we will add them here
        # as we generate them
        self.u = []

        # Creates an empty objective
        self.m.setObjective(0, GRB.MINIMIZE)

        # Creates the complicating constraints
        self.compc = self.m.addConstr(0, GRB.GREATER_EQUAL, self.pp.demand, "cc")
        # Creates the convexity constraints
        self.convc = self.m.addConstr(0, GRB.EQUAL, 1)

    def addColumn(self, solution:tuple):
        """
        Receives the x_i solutions to the subproblems as a tuple and
        i) stores the solution (necessary for calculating the final x solution)
        ii) generates a combined column
        ii) adds it to RMP.
        """
        self.columns.append(solution)
        # We calculate the cost of the combined column and its lhs term in the complicating constraints (we call it w)
        cost = 0
        w = 0
        for i in range(self.pp.n_materials):
            # Since we add combined columns, for each material we add the cost and the consumption.
            cost += self.pp.costs[i] * solution[i]
            w += self.pp.consumption[i] * solution[i]

        # We pass the coefficient of the constraint in which it appears.
        # It appears with coefficient w in the complicating constraints
        # and with coefficient 1 in the convexity constraints.
        # Read the docs here https://www.gurobi.com/documentation/8.1/refman/py_column2.html
        c = Column([w, 1], [self.compc, self.convc])

        # Calculates the index of the new variable
        index = len(self.u) + 1
        # Adds the new variable starting from the column created.
        # Read the docs here https://www.gurobi.com/documentation/8.1/refman/py_model_addvar.html
        self.u.append(
            self.m.addVar(lb=0.0, ub=GRB.INFINITY, obj=cost, vtype=GRB.CONTINUOUS, name=("u" + str(index)), column=c)
        )

    def solve(self):
        self.m.optimize()

    def print(self, file_name):
        """
        Prints the current problem to file in a human-readable format.
        :param file_name: the name of the file where the problem should be printed.
        :return:
        """
        self.m.write(str(file_name) + ".lp")

    def get_objective(self):
        return self.m.objVal

    def get_pi(self):
        # Read here for how to access the attributes of a constraint
        # https://www.gurobi.com/documentation/8.1/refman/attributes.html#sec:Attributes
        return self.compc.Pi

    def get_sigma(self):
        # Read here for how to access the attributes of a constraint
        # https://www.gurobi.com/documentation/8.1/refman/attributes.html#sec:Attributes
        return self.convc.Pi

    def print_u_solution(self):
        """
        Prints the solution to RMP and its objective value.
        :return:
        """
        for i in range(len(self.u)):
            print('%s %g' % (self.u[i].varName, self.u[i].x))
        print('Obj: %g' % self.m.objVal)

    def print_x_solution(self):
        """
        Calculates and prints the x solution from the u solution,
        as well as its objective value.
        :return:
        """
        x = [0 for i in range(self.pp.n_materials)]
        for i in range(len(self.columns)):
            print(self.columns[i])
            print(self.u[i].x)
            for m in range(self.pp.n_materials):
                x[m] = x[m] + self.columns[i][m] * self.u[i].x
        for m in range(self.pp.n_materials):
            print("x_" + str(m) + "=" + str(x[m]))
        print('Obj: %g' % self.m.objVal)
