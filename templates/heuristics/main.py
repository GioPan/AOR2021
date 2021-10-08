from problem import TSP

# We arbitrary load the instance named bays29 and its optimal solution,
tsp = TSP("bays29.tsp","bays29.opt.tour")
print(tsp.get_nodes())
print(tsp.get_optimal_tour())
print(tsp.get_optimal_tour_length())



