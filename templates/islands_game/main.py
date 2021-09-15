from model import IslandsGameModel
from problem import IslandsGame

# Creates an islands game
ig = IslandsGame("instance_4.txt")


igm = IslandsGameModel(ig)

igm.solve()
igm.print_solution()

