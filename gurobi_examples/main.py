from gurobi_examples.cflp.flp import FacilityLocationProblem
from gurobi_examples.cflp.flp_fullproblem import FullModel
from gurobi_examples.cflp.flp_master import Master
import random as r
from gurobi_examples.procurement_problem.procurement_problem import ProcurementProblem
from gurobi_examples.procurement_problem.pp_fullmodel import PPFullModel
from gurobi_examples.procurement_problem.pp_rmp import PPRMP

# =========================================
# Experiments with Benders decomposition on
# the CFLP
# =========================================

# 1. Creates the data
# ===================
n_locations = 5
n_customers = 5

r.seed(1)
# Random fixed costs between 100 and 300
fixed_costs = [(100 + (r.random() * 200)) for i in range(n_locations)]

# Random delivery costs between 10 and 40
delivery_costs = [[(10 + (r.random() * 30)) for j in range(n_customers)] for i in range(n_locations)]

# Random demands between 50 and 100
demands = [(50 + (r.random() * 50)) for j in range(n_customers)]

# Random capacities between 100 and 140
capacities = [(120 + (r.random() * 20)) for i in range(n_locations)]

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


# =========================================
# Experiments with the procurement problem
# =========================================

r.seed(10)
n_materials = 3
costs = [(0 + 10 * r.random()) for i in range(n_materials)]
demand = 100 + 50 * r.random()
consumption = [((100/n_materials) + 50 * r.random()) for i in range(n_materials)]
pmin = [0 for i in range(n_materials)]
pmax = [(20 + 5 * r.random()) for i in range(n_materials)]

# We solve the full problem
pp = ProcurementProblem(n_materials,costs,pmin,pmax,demand,consumption)
ppm = PPFullModel(pp)
ppm.solve()

# We solve the problem by DW
print("Solving DW")
pprmp = PPRMP(pp)
pprmp.solve()

# We compare the solutions
pprmp.print_x_solution()
ppm.print_solution()
