class AlloyProductionProblem:
    """
    This class represents the Alloy Production Problem.
    An instance of this class contains the data for an instance of the Alloy Production Problem.
    """
    def __init__(self,demand:float,min_grade:dict, max_grade:dict,availability:dict,cost:dict,content:dict):
        """
        Creates an instance of the Alloy production problem
        :param demand: the demand of alloy
        :param min_grade: the minimum grade is a dictionary <chemical, percentage>
        :param max_grade: the maximum grade is a dictionary <chemical, percentage>
        :param availability: the available amount of raw materials is a dictionary <material, quantity>
        :param cost: the cost of raw materials is a dictionary <material, cost>
        :param content: the content of chemicals of each raw material is a dictionary <(material,chemical),percentage>
        """
        self.demand = demand
        self.min_grade = min_grade
        self.max_grade = max_grade
        self.availability = availability
        self.cost = cost
        self.content = content
