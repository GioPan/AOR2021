from gurobipy import tuplelist
from stadium_problem import StadiumConstructionProblem
from stadium_model import StadiumConstructionModel

# PROBLEM DATA
tasks = [i for i in range(1,18+1)]
durations = {1: 2,
            2: 16,
            3: 9,
            4: 8,
            5: 10,
            6: 6,
            7: 2,
            8: 2,
            9: 9,
            10: 5,
            11: 3,
            12: 2,
            13: 1,
            14: 7,
            15: 4,
            16: 3,
            17: 9,
            18: 1}

precedences = tuplelist([(2,1),(3,2),(4,2),(5,3),(6,4),(6,5),(7,4),(8,6),(9,4),(9,6),(10,4),(11,6),(12,9),(13,7),(14,2),
                         (15,4),(15,14),(16,8), (16,11),(16,14),(15,11),(17,12),(18,17)])

# Creates an instance of the Stadium Construction Problem
p = StadiumConstructionProblem(tasks,durations,precedences)
# TODO: Create an instance of the model here

# TODO: Solve the model here

# TODO: Print the solution here
