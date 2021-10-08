class FixedChargeTransportationProblem:

    def __init__(self,n_sources:int,n_sinks:int,supply:list,demand:list,transport_costs:dict,fixed_charge:dict):
        self.n_sinks = n_sinks
        self.n_sources = n_sources
        self.supply = supply
        self.demand = demand
        self.transport_cost = transport_costs
        self.fixed_charge = fixed_charge

    def get_max_flow(self,i:int,j:int):
        return min(self.supply[i],self.demand[j])
