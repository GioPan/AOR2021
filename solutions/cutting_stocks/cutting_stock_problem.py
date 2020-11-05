class CuttingStockProblem:

    def __init__(self,width_large_rolls:float, width_small_rolls:list, demand_small_rolls:list):
        self.width_large_rolls = width_large_rolls
        self.width_small_rolls = width_small_rolls
        self.demand = demand_small_rolls

    def get_max_number_of_large_rolls(self):
        '''
        Returns an upper bound on the number of large rolls used.
        It assumes that each small roll is cut from a different large roll,
        therefore, the upper bound is equal to the sum of the demands.
        :return:int
        '''
        return sum(self.demand)

    def get_n_small_roll_types(self):
        return len(self.width_small_rolls)
    def get_feasible_patterns(self):

        # First we calculate how many of each width we can cut from a large roll
        max_rolls = [int((self.width_large_rolls/self.width_small_rolls[i])//1) for i in range(self.get_n_small_roll_types())]

        # Now, we generate all possible patterns, and then we
        # check which ones are feasible. All
        # possible patterns are given by the Cartesian product of
        # the integers up to max_rolls.
        # That is, if we can cut
        # -- up to 2 of width w1, that is 0, 1 or 2
        # -- up to 2 of width w2, that is 0, 2 or 2
        # -- up to 3 of width w3, that is 0, 1, 2 or 3
        # all the possible patters are given by the Cartesian product
        # of the vectors[0, 1, 2]x[0, 1, 2]x[0, 1, 2, 3]
        vectors = {}
        for i in range(self.get_n_small_roll_types()):
            vectors[i] = [j for j in range(max_rolls[i] + 1)]

        patterns = None
        for i in vectors:
            if patterns == None:
                patterns = self.cartesian_product_of_one(vectors[i])
            else:
                patterns = self.cartesian_product_of_two(patterns,vectors[i])

        # Now, of the cartesian products, we discard the elements which violate the large roll width
        infeasible_patterns = []
        for p in patterns:
            cut_width = sum([self.width_small_rolls[i] * p[i] for i in range(self.get_n_small_roll_types())])
            if cut_width > self.width_large_rolls:
                infeasible_patterns.append(p)
        for p in infeasible_patterns:
            patterns.remove(p)

        return patterns

    def cartesian_product_of_one(self,a:list):
        return [(i,) for i in a]

    def cartesian_product_of_two(self,a:list,b:list) -> list:
        elements = []
        for i in a:
            for j in b:
                elements.append(i+(j,))
        return(elements)

