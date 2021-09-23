from model import IslandsGameModel
from problem import IslandsGame

# Creates an islands game
# There are different instances in the folder.
# Change the name of the instance to solve a different instance.
ig = IslandsGame("instance_4.txt")


igm = IslandsGameModel(ig)

igm.solve()
igm.print_solution()

