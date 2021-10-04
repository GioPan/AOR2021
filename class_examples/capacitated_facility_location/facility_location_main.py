from facility_location_problem import FacilityLocationProblem
from facility_location_fullmodel import FullModel
from facility_location_master import Master
import random as r

# =========================================
# Experiments with Benders decomposition on
# the CFLP
# =========================================

# 1. Creates the data
# ===================
n_locations = 15
n_customers = 30

r.seed(1)
# Random fixed costs between 100 and 300
fixed_costs = [(100 + (r.random() * 200)) for i in range(n_locations)]

# Random delivery costs between 10 and 40
delivery_costs = [[(10 + (r.random() * 30)) for j in range(n_customers)] for i in range(n_locations)]

# Random demands between 50 and 100
demands = [(50 + (r.random() * 50)) for j in range(n_customers)]

# Random capacities between 100 and 140
capacities = [(150 + (r.random() * 50)) for i in range(n_locations)]

# 2. Creates an instance of the flp
# =================================
flp = FacilityLocationProblem(n_locations, n_customers, fixed_costs, delivery_costs, demands, capacities)

# 3. Solves the problem by BD
# ===========================
mp = Master(flp)
mp.solve()

# 3. Solves the full problem
# ===========================
m = FullModel(flp)
m.solve()

# 4. Compares the solutions
# ===========================
mp.print_solution()
m.print_solution()


