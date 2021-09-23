from uranium_problem import UraniumMineProblem
from uranium_model import UraniumMineModel
from gurobipy import tuplelist
blocks = [i for i in range(1,19)]
costs = {1: 100,
         2: 100,
         3: 100,
         4: 100,
         5: 100,
         6: 100,
         7: 100,
         8: 100,
         9: 1000,
         10: 200,
         11: 200,
         12: 200,
         13: 200,
         14: 1000,
         15: 1000,
         16: 1000,
         17: 300,
         18: 1000}
values = {1: 200,
         2: 0,
         3: 0,
         4: 0,
         5: 0,
         6: 0,
         7: 300,
         8: 0,
         9: 0,
         10: 500,
         11: 0,
         12: 200,
         13: 0,
         14: 0,
         15: 0,
         16: 0,
         17: 1000,
         18: 1200}

precedences = tuplelist([(9,1),(9,2),(9,3),(10,2),(10,3),(10,4),(11,3),(11,4),(11,5),(12,4),(12,5),(12,6),(13,5),(13,6),(13,7),(14,6),(14,7),(14,8),
               (15,9),(15,10),(15,11),(16,10),(16,11),(16,12),(17,11),(17,12),(17,13),(18,12),(18,13),(18,14)])

p = UraniumMineProblem(blocks,costs,values,precedences)
m = UraniumMineModel(p)
m.solve()
m.printSolution()