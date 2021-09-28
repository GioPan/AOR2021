from gurobipy import Model, GRB
from flp_fsp import FSP
from flp_osp import OSP


class Master:

    def __init__(self, flp):
        # TODO: Create the master problem here

    def solve(self):
	# We need to use a lazy constraints callback
        def callback(model, where):
            if where == GRB.Callback.MIPSOL:
                x_val = model.cbGetSolution(model._x)
                phi_val = model.cbGetSolution(model._phi)

                # TODO: Complete the callback
                # Check feasibility, and add cuts if necessary
		# Check optimality, and add cuts if necessary

        # self.m.setParam(GRB.Param.DisplayInterval, 20)
        self.m.setParam(GRB.Param.LazyConstraints, 1)
        self.m.optimize(callback)

    def print_solution(self):
        for i in range(self.flp.n_facilities):
            print('%s %g' % (self.m._x[i].varName, self.m._x[i].x))
        print('Obj: %g' % self.m.objVal)




