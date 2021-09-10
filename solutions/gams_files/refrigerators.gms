* ****************************************
* Implementation of the Refrigerators Dealer Problem
* Giovanni Pantuso gp@math.ku.dk
* ****************************************

SET month 'the months in the planning horizon' /aug,sep,oct/;


SCALARS
initial_units 'available refrigerators in July' /25/
max_buy 'the maximum number of refrigerators the dealer can buy' /65/
max_sell 'the maximum number of refrigerators the dealer can buy' /100/
storage_cost 'in [$\unit\month]' /7/
storage_capacity 'max number of refs that can be stored' /45/
;

PARAMETERS
cost(month) 'cost of a ref each month [$]'
         /aug 60
         sep 65
         oct 68/

price(month) 'the price of a ref each month [$]'
         /aug 90
         sep 110
         oct 105/
;



VARIABLES
z                'total profit'
s(month)         'number of refs sold'
b(month)         'number of refs bought'
k(month)         'number of refs kept (stored)'
;


POSITIVE VARIABLES
s(month)
b(month)
k(month)
;


EQUATIONS
profit                     'the expression of the total profit'
storage_balance(month)     'the storage balance each month'
sales_ub(month)            'upperbound on the number of sales'
buy_ub(month)              'upperbound on the number of purchases'
storage_ub(month)          'upperbound on the number of refs stored'
;


* Check out how to write summations on the User Guide

profit..       z =e= sum(month, price(month)*s(month)
                 - cost(month)*b(month) - storage_cost*k(month));

* To define the following equation the following features are used:
* - ord operator, as in ord(month),
* - left-hand side dollar sign in assignments to create a different equations
*   depending on whether the mont is august (the first month) or nor
* - the lead operator, as in k(month-1), to refer to the previous member
*   of the set month. Check out pages 115-116 in the user guide

storage_balance(month)..      k(month) =e= (initial_units + b(month)
                                              - s(month))$(ord(month) eq 1)
                                           + (k(month-1) + b(month)
                                              - s(month))$(ord(month) gt 1);

sales_ub(month)..                s(month) =l= max_sell;
buy_ub(month)..                  b(month) =l= max_buy;
storage_ub(month)..              k(month) =l= storage_capacity;


* Sets the maximum CPU time (in seconds)
* the solver can spend to solve the problem
OPTION reslim = 3600;

MODEL dynamic /all/;
SOLVE dynamic USING lp MAXIMIZING z;

DISPLAY
         z.l
         s.l
         b.l
         k.l;

