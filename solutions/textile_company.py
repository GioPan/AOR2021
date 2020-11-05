from gurobipy.gurobipy import Model,GRB

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
m.addConstr(0.3 * xa + 0.5 * xb - yw , sense= GRB.LESS_EQUAL, rhs=0)
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
