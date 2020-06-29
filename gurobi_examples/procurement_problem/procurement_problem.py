class ProcurementProblem:
    """
    Class representing the Procurement Problem.
    An instance of this class contains the data for an instance of
    the procurement problem.
    """

    def __init__(self,n_materials:int,costs:list,min_procurement:list,max_procurement:list,demand:float,consumption:list):
        """
        Creates an instance of the production problem given its data.
        :param n_materials:
        :param costs:
        :param min_procurement:
        :param max_procurement:
        :param demand:
        :param consumption:
        """
        self.n_materials = n_materials
        self.costs = costs
        self.min_production = min_procurement
        self.max_production = max_procurement
        self.demand = demand
        self.consumption = consumption

