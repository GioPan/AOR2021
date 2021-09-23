from gurobipy import GRB, Model

# Data

months = [8,9,10]
cost = {8:60,9:65,10:68}
price = {8:90,9:110,10:105}
max_buy = 65
max_sell = 100
storage_capacity = 45
storage_cost = 7
current_stock = 25

# Model
m = Model('ref')

# Decision variables
b = m.addVars(months,lb=0,ub=max_buy,vtype=GRB.CONTINUOUS,name="b")
s = m.addVars(months,lb=0,ub=max_sell,vtype=GRB.CONTINUOUS,name = "s")
k = m.addVars(months,lb=0,ub=storage_capacity,vtype=GRB.CONTINUOUS,name="k")
print(s)
# Objective function
expr = 0
for i in months:
    expr = expr + price[i] * s[i] - cost[i] * b[i] - storage_cost * k[i]
m.setObjective(expr,sense=GRB.MAXIMIZE)

# Constraints
for i in months:
    if i == 8:
        m.addConstr(k[i]-b[i]+s[i] == current_stock)
    else:
        m.addConstr(k[i]-k[i-1] - b[i]+s[i] == 0)

m.optimize()

print('Objective value: %g' % m.objVal)
for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
