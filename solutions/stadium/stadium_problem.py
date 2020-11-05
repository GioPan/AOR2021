from gurobipy.gurobipy import tuplelist
class StadiumConstructionProblem:
    """
    This class contains the data of the Stadium Construction Problem.
    An instance of this class represents an instance of the problem.
    """
    def __init__(self,tasks: list,durations:dict,precedences:tuplelist):
        self.tasks = tasks
        self.durations = durations
        self.precedences = precedences