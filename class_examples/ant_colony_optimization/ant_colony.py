from problem import TSP
import copy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class AntColonyOptimization:

    def __init__(self,tsp:TSP, population_size:20, n_generations = 500, pheromone_reduction_rate = 0.2):
        self.tsp = tsp
        self.population_size = population_size
        self.n_generations = n_generations
        self.pheromone_reduction_rate = pheromone_reduction_rate
        # Initializes the pheromone
        self.pheromone = {(i,j) : (1/(self.tsp.get_n_nodes()))
        for i in self.tsp.get_nodes() for j in self.tsp.get_nodes() }

    def construct_solution(self):
        # Gets the list of cities not yet in the tour
        cities = copy.deepcopy(self.tsp.get_nodes())
        # Creates an empty list which will be the solution (permutation-based encoding)
        solution = []
        # First it selects a random city
        current_city = np.random.choice(cities)
        # Adds it to the solution
        solution.append(current_city)
        # Removes the current city from the unsequenced cities
        cities.remove(current_city)
        while len(cities) > 0:
            # Selects the next city based on the pheromone
            denominator = sum([self.pheromone[(current_city,j)] for j in cities])
            probabilities = [self.pheromone[(current_city,j)]/denominator for j in cities]
            next_city = np.random.choice(cities, p=probabilities)
            # Adds the city to the solution
            solution.append(next_city)
            # Removes it from the unsequenced cities
            cities.remove(next_city)
            # Updates the current solution
            current_city = next_city
        return solution

    def evaporate_pheromone(self):
        for (i,j) in self.pheromone.keys():
            self.pheromone[(i,j)] = self.pheromone[(i,j)] * (1 - self.pheromone_reduction_rate)

    def update_pheromone(self,solution:list):
        # Calculates the cost of the solution
        cost = self.tsp.get_tour_length(solution)
        # Updates the pheromone
        # Gets the (i,j) for which there exists an arc in the solution
        for position in range(len(solution)-1):
            i = solution[position]
            j = solution[position+1]
            self.pheromone[(i,j)] = self.pheromone[(i,j)] + 1/cost

    def plot_pheromone(self):
        # Transforms the pheromone dict into a matrix
        data = [[self.pheromone[(i,j)] for j in self.tsp.get_nodes()] for i in self.tsp.get_nodes()]
        # Plot the pheromone
        ax = sns.heatmap(data, linewidth=0.5)
        plt.show()

    def generate_population(self) -> list:
        population = []
        for i in range(self.population_size):
            solution = self.construct_solution()
            population.append(solution)
        return population

    def search(self):
        current_population = None
        for n in range(self.n_generations):
            print("Generation #",n)
            current_population = self.generate_population()
            for s in current_population:
                self.update_pheromone(s)
            self.evaporate_pheromone()
            # Updates the plot
        # Shows the pheromone plot
        return current_population




