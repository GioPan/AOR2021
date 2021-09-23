import random as r
from fsp_problem import FacilitySizingProblem

# =========================================
# Experiments with Benders decomposition on
# the Facility Sizing Problem
# =========================================

# 1. Creates the data
# ===================
n_locations = 5
n_customers = 5

r.seed(1)
# Random capacity costs between 100 and 300
fixed_costs = [(100 + (r.random() * 200)) for i in range(n_locations)]

# Random delivery costs between 10 and 40
delivery_costs = [[(10 + (r.random() * 30)) for j in range(n_customers)] for i in range(n_locations)]

# Random demands between 50 and 100
demands = [(50 + (r.random() * 50)) for j in range(n_customers)]

# Random capacities between 100 and 140
capacities = [(120 + (r.random() * 20)) for i in range(n_locations)]

# 2. Creates an instance of the flp
# =================================
fsp = FacilitySizingProblem(n_locations, n_customers, fixed_costs, delivery_costs, demands, capacities)

# ===========================
# 3. Solves the problem by BD
# ===========================
# TODO Starts here
# 3.1 Create an instance of the MP (you will need to create its class before) given fsp

solved = False
while not solved:
    # 3.2 Solve MP

    # 3.3 Get the x and phi solution from MP

    # 3.4 Create an instance of the Feasibility Subproblem (FSP) given x (you will need its class before)

    # 3.5 Solve FSP

    # 3.6 Get the objective value (say fsp_obj), and optimal dual solution from FSP

    if fsp_obj > 0:
        # 3.7 Add a feasibility cut to MP
        
    else:
        
        # 3.8 Create an instance of the Optimality Subproblem (OSP) given x (you will need its class before)
        
	# 3.9 Solve OSP
        
        # 3.10 Get the objective value (say osp_obj), and optimal dual solution from OSP

        if phi >= osp_obj - 1e-6 :
            print("Problem solved")
            solved = True
        else:
            # 3.11 Add an optimality cut to MP








# 4. Solves the full problem
# ===========================
m = FullModel(fsp)
m.solve()

# 5. Compares the solutions
# ===========================
print("Solution BD")
#mp.print_solution()
print("Solution Original")
m.print_solution()
