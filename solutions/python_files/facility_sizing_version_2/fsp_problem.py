class FacilitySizingProblem:

    def __init__(self,n_facilities:int,n_customers:int,fixed_costs:list,delivery_costs:list,demands:list,capacity:list, special_locations:list,percentage_from_special_locations:float):
        self.n_facilities = n_facilities
        self.n_customers = n_customers
        self.fixed_costs = fixed_costs
        self.delivery_costs = delivery_costs
        self.demands = demands
        self.capacity = capacity
        self.special_locations = special_locations
        self.percentage_from_special_locations = percentage_from_special_locations