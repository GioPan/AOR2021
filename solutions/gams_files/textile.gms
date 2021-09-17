* ****************************************
* IMPLEMENTATION OF THE TEXTILE PRODUCTION PROBLEM
* Giovanni Pantuso gp@math.ku.dk
* ****************************************
SETS

i 'set of fabric types' /plain,patterned/
j 'set of production inputs' /wool,loom,finishing/;

PARAMETERS

b(j) 'availability of input j'
         /wool 20
         loom 300
         finishing 200/

p(i) 'profit of fabric i in m^2'
         /plain 60
          patterned 65/
c(j) 'cost of input j'
         /wool 3
         loom 3
         finishing 10/


TABLE a(i,j) 'requirement of input j in the production of fabric i'
                         wool    loom    finishing
         plain           0.3     6       3
         patterned       0.5     5       5;


VARIABLES
z        'total profit'
x(i)     'amount of fabric i produced'
y(j)     'amount of input j purchased'
;


POSITIVE VARIABLES
x(i)
y(j);


EQUATIONS
cost                     'the expression of the total profit'
consumption(j)           'the amount of input j consumed'
purchase(j)              'the amount of input j purchased'
;



cost ..                  z =e= sum(i, p(i)*x(i))- sum(j, c(j)*y(j));
consumption(j)..         sum(i,a(i,j)*x(i)) =l= y(j);
purchase(j)..            y(j) =l= b(j);



*OPTION reslim = 1e10;
*OPTION limcol = 2;
OPTION limrow = 3;

MODEL production /all/;
SOLVE production USING lp MAXIMIZING z;

DISPLAY
         x.l
         y.l
         z.l;

