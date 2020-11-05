
from solutions.bd_example1.bd_full_model import FullModel
from solutions.bd_example1.bd_mp import MP
from solutions.bd_example1.bd_osp import OSP
from solutions.bd_example1.bd_fsp import FSP
solved = False
mp = MP()

while not solved:
    mp.solve()
    x,phi = mp.get_sol()
    mp.write_model()
    print(x,phi)
    # Check feasibility
    fsp = FSP(x)
    fsp.solve()
    fsp_obj, fsp_pi1,fsp_pi2 = fsp.get_results()
    print("FSP ",fsp_obj,fsp_pi1,fsp_pi2)
    if fsp_obj > 0:
        print("Adding feasibility cut")
        mp.add_feasibility_cuts(fsp_pi1,fsp_pi2)
    else:
        osp = OSP(x)
        osp.solve()
        osp_obj, osp_pi1, osp_pi2 = osp.get_results()
        print("OSP ", osp_obj, osp_pi1, osp_pi2)
        print("Phi ",phi)
        if phi >= osp_obj:
            solved = True
        else:
            mp.add_optimality_cuts(osp_pi1,osp_pi2)

mp.print_solution()
mp.write_model()

m = FullModel()
m.solve()
m.print_solution()
