import random
from gurobipy import Model, GRB, quicksum, tuplelist, tupledict
class IslandsGame:

    def __init__(self,file:str):
        self.islands = {}
        with open(file) as f:
            # Reads the size of the game
            self.N = int(f.readline())
            print(self.N)
            # Reads the island belonging to which each cell belongs
            for i in range(self.N):
                for j in range(self.N):
                    # We read the line
                    line = f.readline()
                    # The input of each line is of type i j k where k is the island
                    # We split the line into the three values using the method split() which returns a list
                    # of type [i,j,k]. We are interested in k, so we read the 3rd element of the list.
                    island = int(line.split()[2])
                    self.islands[(i,j)] = island

        for i in range(self.N):
            for j in range(self.N):
                print("%3d "% self.islands[(i,j)], end="")
            print()






