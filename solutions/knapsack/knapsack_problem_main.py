from solutions.knapsack.knapsack_problem import KnapsackProblem
from solutions.knapsack.knapsack_problem_model import KnapsackProblemModel
from solutions.knapsack.knapsack_problem_lp_model import KnapsackProblemLPModel


capacity = 50
weights = [10, 24, 25, 2, 15,9]
rewards = [5, 9, 8, 1, 7,6]

p = KnapsackProblem(capacity,weights,rewards)

# Cover contains the indices of the items in the cover
cover1 = [0,1,2]
rhs1 = 2
cover2 = [0,1,4,5]
rhs2 = 3

# Solves the ip problem
m = KnapsackProblemModel(p)
# Outcomment the cover you want to add
#m.addCover(cover1,rhs1)
m.addCover(cover2,rhs2)
m.solve()
m.printSolution()

# Solves the lp relaxation
lp = KnapsackProblemLPModel(p)
# Outcomment the cover you want to add
#lp.addCover(cover1,rhs1)
lp.addCover(cover2,rhs2)
lp.printModel()
lp.solve()
lp.printSolution()