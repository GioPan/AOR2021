import math
import random as rd
rd.seed(1)
from fctp_problem import FixedChargeTransportationProblem
from fctp_fullmodel import FullModel
from fctp_master import Master

# 1. We generate a random instance of the problem
n_sources = 3
n_sinks = 9

# We need to ensure that total supply equals total demand
supply = [rd.randint(20,40) for i in range(n_sources)]
total_supply = sum(supply)
# Now we assign demand such that they sum to the total supply
# We first randomly assign demand to n_sink-1 and the the remaining to the last sink
demand = [rd.randint(math.floor(total_supply/n_sinks)-5,math.floor(total_supply/n_sinks)+5) for j in range(n_sinks-1)]
demand.append(total_supply-sum(demand))
transport_cost = {(i,j) : rd.randint(2,8) for i in range(n_sources) for j in range(n_sinks)}
fixed_charge = {(i,j) : rd.randint(15,28) for i in range(n_sources) for j in range(n_sinks)}

# TODO: CREATE AN INSTANCE OF THE FIXED CHARGE TRANSPORTATION PROBLEM


# TODO: SOLVE THE PROBLEM VIA BENDERS DECOMPOSITION

# TODO: SOLVE THE FULL MODEL (I.E., WITHOUT DECOMPOSITION)

# TODO: PRINT THE SOLUTION TO THE FULL PROBLEM AND TO BD

