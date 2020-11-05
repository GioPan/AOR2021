from solutions.cutting_stocks.cutting_stock_model1 import CuttingStockModel1
from solutions.cutting_stocks.cutting_stock_model2 import CuttingStockModel2
from solutions.cutting_stocks.cutting_stock_problem import CuttingStockProblem
from solutions.cutting_stocks.cutting_stock_model1_lp import CuttingStockModel1LP
from solutions.cutting_stocks.cutting_stock_model2_lp import CuttingStockModel2LP
width_large_rolls = 5
width_small_rolls = [2.1,1.8,1.5]
demand_small_rolls = [9,12,19]

p = CuttingStockProblem(width_large_rolls,width_small_rolls,demand_small_rolls)


m1 = CuttingStockModel1(p)
m1.solve()
m1.print_solution()


m2 = CuttingStockModel2(p)
m2.solve()
m2.print_solution()

# LP Relaxations
m1lp = CuttingStockModel1LP(p)
m1lp.solve()
m1lp.print_solution()


m2lp = CuttingStockModel2LP(p)
m2lp.solve()
m2lp.print_solution()
