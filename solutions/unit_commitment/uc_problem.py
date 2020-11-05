class UnitCommitmentProblem:
    '''
    This class represents the blueprint of the Unit Commitment Problem.
    '''

    def __init__(self,power_lb: dict, power_ub : dict, start_up_cost:dict,
                 commitment_cost:dict,ramping_limit : dict,
                 min_uptime: dict,min_downtime:dict,production_cost:dict, loads:dict,shedding_cost:float):
        self.generators = power_lb.keys()
        self.hours = loads.keys()
        # TODO: Write the constructor

    # TODO: write here all additional methods you might need from this class
