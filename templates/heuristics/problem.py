import tsplib95



class TSP:
    '''
    Objects of this class represent instances of the Traveling Salesman Problem (see the Classical Problems Library).
    The data of the instances is provided files contained in the tsp_instances folder and read by the package tsplib95.
    The package is described here https://pypi.org/project/tsplib95/
    and the data of the instances is taken from a set of known benchmark instances (the TSPLIB 95 library)
    which are made available at this link http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/.
    In the TSPLIB there are several instances of various sizes. For several instances the library provides also the
    optimal solution, if it is known (some instances are so difficult that the optimal solution has not yet been found).
    In our example we will use a small instance for which we know the optimal solution.
    '''

    def __init__(self,instance_name:str, optimal_tour:str):
        '''
        Generates the data of the instance given the name of the file
        containing the data of the instance and the name of the file containing the optimal solution.
        '''
        self.data = tsplib95.load('tsp_instances/'+ instance_name)
        self.optimal_tour = tsplib95.load('tsp_instances/' + optimal_tour)

    def get_nodes(self):
        '''
        Returns the list of nodes.
        '''
        return list(self.data.get_nodes())

    def get_distances(self):
        '''
        Returns the distances matrix.
        '''
        return self.data.edge_weights

    def get_distance(self,i:int,j:int):
        '''
        Returns the distance between given nodes i and j.
        '''
        return self.data.get_weight(i,j)

    def get_node_coordinates(self,i:int):
        '''
        Returns the coordinates of the nodes.
        '''
        print(self.data.node_coords)

    def get_n_optimal_tours(self):
        '''
        Returns the list of optimal tours (there may be more than one, though often only one).
        '''
        return len(self.optimal_tour.tours)

    def get_optimal_tour(self,n_tour=0):
        '''
        Returns a specific optimal tour (with no arguments returns the first).
        '''
        return self.optimal_tour.tours[n_tour]

    def get_optimal_tour_length(self,n_tour=0):
        '''
        Returns the length (objective value) of an optimal tour (default the first tour).
        '''
        return self.get_tour_length(self.optimal_tour.tours[0])

    def get_tour_length(self, tour:list):
        '''
        Calculates the length (objective value) of a tour we pass as an argument.
        Note that the tour is first added to a list since the method trace_tours accepts only lists of tours.
        '''
        tour_list = [tour]
        return self.data.trace_tours(tour_list)