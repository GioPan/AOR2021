from gurobipy import  Model,GRB

# Create the model object
m = Model('diet_problem')

# Create the variables
xa = m.addVar(0,GRB.INFINITY,vtype=GRB.CONTINUOUS,name="xa")
xb = m.addVar(0,GRB.INFINITY,vtype=GRB.CONTINUOUS,name="xb")
# a different way to create a non-negative continuous variable
xc = m.addVar(name="xc")
xd = m.addVar(0,GRB.INFINITY,name="xd")
xe = m.addVar(name="xe")

# Create the objective function
expr = 8 * xa + 10 * xb + 3 * xc + 20 * xd + 15 * xe
m.setObjective(expr,sense= GRB.MINIMIZE)

# Create the constraints. We will use different ways of adding a constraint
expr = 0.4 * xa + 1.2 * xb + 0.6 * xc + 0.6 * xd + 12.2 * xe
m.addConstr(lhs= expr,sense= GRB.GREATER_EQUAL,rhs=70)
m.addConstr(6 * xa + 10* xb + 3 * xc + 1 * xd +0 * xe >= 50)
m.addConstr(0.4 * xa + 0.6 * xb + 0.4 * xc + 0.2 * xd + 2.6*xe, GRB.GREATER_EQUAL,12)


m.optimize()

print('Objective value: %g' % m.objVal)
print('%s %g' % (xa.varName, xa.x))
print('%s %g' % (xb.varName, xb.x))
print('%s %g' % (xc.varName, xc.x))
print('%s %g' % (xd.varName, xd.x))
print('%s %g' % (xe.varName, xe.x))