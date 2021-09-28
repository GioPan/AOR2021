# ====================================================
# This is the main file which provides an entry point
# to your application.
# ====================================================

# 1. DATA COLLECTION
# In the first part of this file we collect and arrange the data of the problem

# 1.1 We create the containers of the data of the problem
# Data of generators and loads may be stored in dictionaries
power_lb = {}
power_ub = {}
start_up_cost = {}
commitment_cost = {}
ramping_limit = {}
min_uptime = {}
min_downtime = {}
production_cost = {}
loads = {}

# 1.2 Reads the data of the generators from its file
# Change the path to the generators file if you put it in a different folder
generators_file = "path/to/the/location/of_the_file/loads.txt"
# Here you are given an example of how to read the generators file
# and assign the date to the dictonaries above.
with open(generators_file) as f:
    line_counter = 1
    for line in f:
        # Skips the first two lines (the header of the file)
        if line_counter > 2:
            # The following line reads all elements in a line.
            # If it starts by U it returns a string otherwise a float
            name, lb, ub, su_cost, comm_cost, ramping_lim, min_up, min_down, prod_cost = (float(n) if not n.startswith("U") else n for n in line.split())
            power_lb[name]= lb
            power_ub[name] = ub
            start_up_cost[name] = su_cost
            commitment_cost[name] = comm_cost
            ramping_limit[name]= ramping_lim
            min_uptime[name] = min_up
            min_downtime[name] = min_down
            production_cost[name] = prod_cost
            line_counter = line_counter + 1
        else:
            line_counter = line_counter + 1

# 1.3 TODO: Calculate the shedding cost a 2 * the highest production cost

# 1.4. TODO: Read load data
loads_file = "path/to/the/location/of_the_file/loads.txt"

# Continue here ...

# 2. CREATE THE PROBLEM
# 2.1 TODO: Create an instance of the class that represents the UCP


# 3. SOLVE THE PROBLEM BY BENDERS DECOMPOSITION
# 3.1 TODO: Write here all the code needed to solve the instance of the UCP by BD

# 4. SOLVE THE PROBLEM WITHOUT DECOMPOSITION
# 4.1 TODO: Write here all the code needed to solve the instance of the UCP without applying a decomposition

# 5. COMPARE THE SOLUTIONS
# 5.1. TODO: Print the optimal objective value of BD and of the full model and show that they are the same.
# 5.1. TODO: Print the optimal solution of BD and of the full model and show that they are the same.
