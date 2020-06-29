class FacilityLocationProblem:

    def __init__(self,n_facilities,n_customers,fixed_costs,delivery_costs,demands,capacity):
        self.n_facilities = n_facilities
        self.n_customers = n_customers
        self.fixed_costs = fixed_costs
        self.delivery_costs = delivery_costs
        self.demands = demands
        self.capacity = capacity