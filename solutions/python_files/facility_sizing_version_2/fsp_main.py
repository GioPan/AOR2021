import random as r
from fsp_problem import FacilitySizingProblem
from fsp_mp import Master
from fsp_feasibilitysp import FSP
from fsp_optimalitysp import OSP
from fsp_fullmodel import FullModel
# =========================================
# Experiments with Benders decomposition on
# the Facility Sizing Problem
# =========================================

# 1. Creates the data
# We randomly generate data for the facility sizing problem
# ===================
n_locations = 5
n_customers = 5

special_locations = [0,2]
percentage_from_special_locations = 0.1

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
fsp = FacilitySizingProblem(n_locations, n_customers, fixed_costs, delivery_costs, demands, capacities,special_locations,percentage_from_special_locations)

# ===========================
# 3. Solves the problem by BD
# ===========================
mp = Master(fsp)
solved = False
while not solved:
    # Solve MP
    mp.solve()

    # Get the x solution
    x, phi = mp.get_solution()

    # Check feasibility by solving the fsp
    feasibility_sp = FSP(fsp,x)
    feasibility_sp.solve()
    fsp_obj, fsp_dualsCC, fsp_dualsDC, dualsPC = feasibility_sp.getResults()
    print("FSP obj ", fsp_obj)
    if fsp_obj > 0:
        # In this case we need a feasibility cut
        print("Adding a feasibility cut")
        mp.add_feasibility_cut(fsp_dualsCC,fsp_dualsDC, dualsPC)
    else:
        print("Checking optimality")
        # In this case we can check optimality
        optimality_sp = OSP(fsp,x)
        optimality_sp.solve()
        osp_obj, osp_dualsCC, osp_dualsDC, dualsPC = optimality_sp.getResults()
        print("Phi = ",phi)
        print("Obj = ", osp_obj)
        if phi >= osp_obj - 1e-6 :
            print("Problem solved")
            solved = True
        else:
            # In this case we add an optimality cut
            mp.add_optimality_cut(osp_dualsCC, osp_dualsDC, dualsPC)







# 3. Solves the full model
# We solve the model without decomposition to check whether the result of
# our Benders decomposition method is correct.
# ===========================
m = FullModel(fsp)
m.solve()

# 4. Compares the solutions
# ===========================
print("Solution BD")
mp.print_solution()
print("Solution Original Problem")
m.print_solution()
