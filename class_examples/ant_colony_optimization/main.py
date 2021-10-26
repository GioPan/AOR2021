from problem import TSP
from ant_colony import AntColonyOptimization
import numpy as np
tsp = TSP("bays29.tsp","bays29.opt.tour")
#tsp = TSP("berlin52.tsp","berlin52.opt.tour")
print(tsp.get_nodes())
print(tsp.get_optimal_tour())
print(tsp.get_optimal_tour_length())

aco = AntColonyOptimization(tsp,50,100)
solutions = aco.search()
best_solution = None
best_cost = float('inf')
for s in solutions:
    cost = tsp.get_tour_length(s)
    if cost < best_cost:
        best_cost = cost
        best_solution = s

print(best_solution)
print("Cost ",best_cost)
aco.plot_pheromone()



