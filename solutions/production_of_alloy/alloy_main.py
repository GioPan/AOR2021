from solutions.production_of_alloy.alloy_problem import AlloyProductionProblem
from solutions.production_of_alloy.alloy_model import AlloyProductionModel

# Creates the data
demand = 500
min_grade = {'carbon':2, 'copper':0.4, 'manganese':1.2}
max_grade = {'carbon':3, 'copper':0.6, 'manganese':1.65}
availability = {'iron1':400, 'iron2':300, 'iron3':600, 'copper1':500,'copper2':200,'alumin1':300,'alumin2':250}
cost = {'iron1':200, 'iron2':250, 'iron3':150, 'copper1':220,'copper2':240,'alumin1':200,'alumin2':165}
content = {('carbon','iron1'):2.5,
           ('carbon','iron2'):3.0,
           ('carbon','iron3'):0,
           ('carbon','copper1'):0,
           ('carbon','copper2'):0,
           ('carbon','alumin1'):0,
           ('carbon','alumin2'):0,
           ('copper','iron1'):0,
           ('copper','iron2'):0,
           ('copper','iron3'):0.3,
           ('copper','copper1'):90,
           ('copper','copper2'):96,
           ('copper','alumin1'):0.4,
           ('copper','alumin2'):0.6,
           ('manganese','iron1'):1.3,
           ('manganese','iron2'):0.8,
           ('manganese','iron3'):0,
           ('manganese','copper1'):0,
           ('manganese','copper2'):4,
           ('manganese','alumin1'):1.2,
           ('manganese','alumin2'):0
           }

# Creates an instance of the problem
p = AlloyProductionProblem(demand,min_grade,max_grade,availability,cost,content)
m = AlloyProductionModel(p)
m.solve()
m.print_solution()
