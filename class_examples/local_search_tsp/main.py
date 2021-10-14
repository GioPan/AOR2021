from problem import TSP
from local_search import LocalSearch

# We arbitrary load the instance named bays29 and its optimal solution,
tsp = TSP("bays29.tsp","bays29.opt.tour")
#tsp = TSP("berlin52.tsp","berlin52.opt.tour")
print(tsp.get_nodes())
print(tsp.get_optimal_tour())
print(tsp.get_optimal_tour_length())

ls = LocalSearch(tsp=tsp)
initial_solution = ls.generate_inital_solution()
print(initial_solution)
print("Cost initial solution", tsp.get_tour_length(initial_solution))

local_optima = ls.solve_with_first_improvement(initial_solution)
print(local_optima)
print("Cost local optima",tsp.get_tour_length(local_optima))

