from problem import TSP
import copy
import random

class LocalSearch:

    def __init__(self,tsp:TSP):
        self.tsp = tsp

    def generate_inital_solution(self):
        '''
        Does the following:
        (i) Gets the list of nodes of the tsp problem
        (ii) Makes a deep copy of the list of nodes.
        This ensures that by changing the order in the initial solution we
        do not modify the list of nodes in the tsp class.
        (iii) performs a random permutation of the nodes
        '''
        # Gets the nodes
        nodes = self.tsp.get_nodes()
        # Makes a deep copy
        initial_solution = copy.deepcopy(nodes)
        # Shuffles them
        random.shuffle(initial_solution)
        return initial_solution



    def swap(self,solution:list, i:int, j:int):
        '''
        Swaps the elements in position i and j in the given solution.
        Dows the following:
        (i) Makes a deep copy of the solution, so that we return a different list
        (ii) Keeps track of the elements in position i and j
        (iii) Swaps them
        '''
        new_solution = copy.deepcopy(solution)
        element_i = new_solution[i]
        element_j = new_solution[j]
        new_solution[i] = element_j
        new_solution[j] = element_i
        return new_solution



    def find_first_improving_solution(self,solution:list):
        current_solution = copy.deepcopy(solution)
        cost_current_solution = self.tsp.get_tour_length(current_solution)
        print("Cost current solution ", cost_current_solution)
        found_improving_solution = False
        for (i, j) in [(a, b) for a in range(len(current_solution)) for b in range(len(current_solution)) if a > b]:
            new_solution = self.swap(current_solution, i, j)
            cost_new_solution = self.tsp.get_tour_length(new_solution)

            if cost_new_solution < cost_current_solution:
                print("Found improving solution with cost", cost_new_solution)
                current_solution = new_solution
                found_improving_solution = True
                # When the first improving solution is found it breaks the loop
                # so that it stops looking for new solutions
                break
        return found_improving_solution, current_solution



    def solve_with_first_improvement(self,initial_solution:list):
        current_solution = copy.deepcopy(initial_solution)
        improving_solution = True
        iteration = 0;
        while improving_solution and (iteration < 500):
            print("Iteration ",iteration)
            improving_solution = False
            iteration += 1
            found_improving_solution, new_solution = self.find_first_improving_solution(current_solution)
            if found_improving_solution:
                improving_solution = found_improving_solution
                current_solution = new_solution
            else:
                print("No improving solution found")
        return current_solution



