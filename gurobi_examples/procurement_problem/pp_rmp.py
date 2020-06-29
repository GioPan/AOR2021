from gurobipy.gurobipy import Model, GRB, Column
from procurement_problem.pp_subproblem import PPSP
from procurement_problem.procurement_problem import ProcurementProblem


class PPRMP():

    def __init__(self, pp: ProcurementProblem):
        """
        Builds an instance of the DW's RMP for the
        Procurement Problem.
        :param pp:
        """

        # Builds an instance of the model
        self.m = Model()
        self.pp = pp

        # Here we will store the columns
        self.columns = []
        # Initially the is no variable,
        # but will will add them here
        # as we generate them
        self.u = []

        # Creates an empty objective
        self.m.setObjective(0, GRB.MINIMIZE)

        # Creates the complicating constraints
        self.compc = self.m.addConstr(0, GRB.GREATER_EQUAL, self.pp.demand, "cc")
        # Creates the convexity constraints
        self.convc = self.m.addConstr(0, GRB.EQUAL, 1)

    def addColumn(self, solution):
        """
        Receives the x_i solutions to the subproblems, generates
        a column in terms of its cost and consumption, and finally
        adds it to RMP.
        """

        # We calculate the cost of the column and its w
        cost = 0
        w = 0
        for i in range(self.pp.n_materials):
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
        """
        Implements the DW algorithm.
        :return:
        """

        # 0. We create a list that will include all columns added during
        # the course of the algorithm. We store columns in terms of their
        # x_i coordinates, for i in 1...n_materials. Therefore each column
        # will be a tuple of n_materials elements. Tuples will be added to the following
        # list of all tuples.
        self.columns = []

        # 1. Initializes RMP with 2 arbitrarily chosen columns.
        # The two columns should represent extreme points of the
        # subproblems.
        c1 = (self.pp.max_production[0], self.pp.max_production[1], self.pp.max_production[2])
        self.addColumn(c1)
        self.columns.append(c1)
        c2 = (self.pp.max_production[0], self.pp.max_production[1], 0)
        self.addColumn(c2)
        self.columns.append(c2)

        # 2. Here the DW algorithm begins
        solved = False
        iteration = 0
        while not solved:
            # Solves RMP
            self.m.optimize()

            # Gets pi and sigma.
            # Read here for how to access the attributes of a constraint
            # https://www.gurobi.com/documentation/8.1/refman/attributes.html#sec:Attributes
            pi = self.compc.pi
            sigma = self.convc.pi

            # Solves the subproblems
            # We store the solutions in a tuple
            # with one element for each subproblem
            # e.g., (x_1,x_2,x_3)
            new_col = tuple()
            for p in range(self.pp.n_materials):
                # Creates and solves the subproblem
                sp = PPSP(self.pp, p, pi)
                sp.solve()

                # Adds the solution for product p
                # to the solution tuple
                new_col = new_col + (sp.get_solution(),)

            # Does the optimality test
            # Calculates delta = sum_j(c_j - pi A_j)x_j - sigma_j
            delta = 0
            for p in range(self.pp.n_materials):
                delta = delta + self.pp.costs[p] * new_col[p]
                delta = delta - (pi * self.pp.consumption[p]) * new_col[p]
            delta = delta - sigma

            if delta >= 0:
                # If delta > 0 we are not missing any column
                print("Problem solved!".upper())
                solved = True
            else:
                # Otherwise we add the column we have just generated
                self.columns.append(new_col)
                self.addColumn(new_col)

    def print(self, file_name):
        """
        Prints the current problem to file in a human-readable format.
        :param file_name: the name of the file where the problem should be printed.
        :return:
        """
        self.m.write(str(file_name) + ".lp")

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
            for p in range(self.pp.n_materials):
                x[p] = x[p] + self.columns[i][p] * self.u[i].x
        for p in range(self.pp.n_materials):
            print("x_" + str(p) + "=" + str(x[p]))
        print('Obj: %g' % self.m.objVal)
