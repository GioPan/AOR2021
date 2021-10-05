import random as r
from pp_problem import ProcurementProblem
from pp_fullmodel import PPFullModel
from pp_rmp import RMP
from pp_subproblem import PPSP

# =========================================
# Experiments with the procurement problem
# =========================================

# Creates the data of the problem


r.seed(10)
n_materials = 15
costs = {i: (0 + 10 * r.random()) for i in range(n_materials)}
demand = 100 + 50 * r.random()
consumption = {i: ((100/n_materials) + 50 * r.random()) for i in range(n_materials)}
pmin = [0 for i in range(n_materials)]
pmax = [(20 + 5 * r.random()) for i in range(n_materials)]

# Creates an instance of the procurement problem
pp = ProcurementProblem(n_materials,costs,pmin,pmax,demand,consumption)

# Creates and solves an instance of the full problem
ppm = PPFullModel(pp)
ppm.solve()

# Creates an instance of the RMP and solves the problem by DW
rmp = RMP(pp)

# 1. Initializes RMP with 2 arbitrarily chosen columns.
# The two columns should represent extreme points of the
# subproblems. In this case it easy to find extreme points of the sets S_m
# since each set S_m has two extreme points: Q^Max_m and Q^Min_m (or 0).

solution1 = tuple(pp.max_procurement[i] for i in range(pp.n_materials))
rmp.addColumn(solution1)

solution2 = tuple(pp.min_procurement[i] for i in range(pp.n_materials))
rmp.addColumn(solution2)

# 2. Here the DW algorithm begins
solved = False
while not solved:
    # TODO Solves RMP
    #
    print("Upper bound = ",rmp.get_objective())
    
    # TODO Gets pi and sigma.
    
    # Solves the subproblems
    # We store the solutions in a tuple (this is an arbitrary decision)
    # with one element for each subproblem, e.g., (x_1,x_2,x_3)
    solutions = tuple()
    lower_bound = 0
    for m in range(pp.n_materials):
        # TODO Creates and solves the subproblem
        
        # Adds a term to the lower bound
        lower_bound = lower_bound + sp.get_objective()
        # Adds the solution for material m
        # to the solution tuple
        solutions = solutions + (sp.get_solution(),)

    lower_bound = lower_bound + pi * pp.demand
    print("Lower bound = ",lower_bound)

    # Optimality test
    # Calculates delta = sum_j(c_j - pi A_j)x_j - sigma_j
    delta = 0
    for m in range(pp.n_materials):
        delta = delta + pp.costs[m] * solutions[m]
        delta = delta - (pi * pp.consumption[m]) * solutions[m]
    delta = delta - sigma

    if delta >= 0:
        # If delta > 0 we are not missing any column
        print("Problem solved!".upper())
        solved = True
    else:
        # Otherwise we add the column we have just generated
        # TODO: ADD new column to RMP


# Prints the solutions
rmp.print_x_solution()
ppm.print_solution()
