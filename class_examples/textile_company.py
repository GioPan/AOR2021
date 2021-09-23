from gurobipy import Model,GRB

# Model
m = Model('textile')

# Decision variables
xa = m.addVar(0,GRB.INFINITY,vtype=GRB.CONTINUOUS,name="xa")
xb = m.addVar(0,GRB.INFINITY,vtype=GRB.CONTINUOUS,name="xb")
yw = m.addVar(0,GRB.INFINITY,vtype=GRB.CONTINUOUS,name="yw")
yl = m.addVar(0,GRB.INFINITY,vtype=GRB.CONTINUOUS,name="yl")
yh = m.addVar(0,GRB.INFINITY,vtype=GRB.CONTINUOUS,name="yh")

# Objective function
m.setObjective(60 * xa + 65 * xb - 3 * yw - 3 * yl - 10 * yh, sense= GRB.MAXIMIZE )

# Constraints
constr1 = m.addConstr(0.3 * xa + 0.5 * xb - yw , sense= GRB.LESS_EQUAL, rhs=0)
m.addConstr(6 * xa + 5 * xb <= yl)
m.addConstr(3 * xa + 5 * xb <= yh)
m.addConstr(yw <= 20)
m.addConstr(yl <= 300)
m.addConstr(yh <= 200)

m.optimize()

print('Objective value: %g' % m.objVal)
print('%s %g' % (xa.varName, xa.x))
print('%s %g' % (xb.varName, xb.x))
print('%s %g' % (yw.varName, yw.x))
print('%s %g' % (yl.varName, yl.x))
print('%s %g' % (yh.varName, yh.x))

# We can obtain the same information using the model getAttr of the model object.
# In this case we need to pass the list of variables we are interested in
print("Variable names and values")
print(m.getAttr('varName', [yh]))
print(m.getAttr('x', [yh]))

print(m.getAttr('varName', [yh,yw]))
print(m.getAttr('x', [yh,yw]))

# Solution information
print("# Variables ", m.getAttr("NumVars"))
print("# Integer Variables ", m.getAttr("NumIntVars"))
print("# Constraints ", m.getAttr("NumConstrs"))

print("# Variables ", m.NumVars)
print("# Integer Variables ", m.NumIntVars)
print("# Binary Variables ", m.NumBinVars)
print("# Constraints ", m.NumConstrs)

# Duals
# Note that we need to assing the constraint to a variable, as we did with constr1
print('Dual = %g' % constr1.Pi)