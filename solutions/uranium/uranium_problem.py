from gurobipy.gurobipy import tuplelist
class UraniumMineProblem:
    """
    This class contains the data of the Uranium Mine Problem.
    An instance of this class represents an instance of the problem.
    """
    def __init__(self,blocks: list,costs:dict,values:dict,precedences:tuplelist):
        self.blocks = blocks
        self.costs = costs
        self.values = values
        self.precedences = precedences
