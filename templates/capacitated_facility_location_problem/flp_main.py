# Necessary imports
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

# 2. TODO: Create an instance of the flp
# =================================

# 3. TOD: Solve the problem by BD
# ===========================

# 4. TODO: Solve the full problem
# ===========================


# 5. Compares the solutions
# ===========================


