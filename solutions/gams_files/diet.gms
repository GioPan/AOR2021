* ****************************************
* IMPLEMENTATION OF THE DIET PROBLEM
* Giovanni Pantuso gp@math.ku.dk
* 
* Find the minimum cost diet that satisfies
* nutritional needs
*
* x_i = amount of food i in the diet
* c_i = cost of food i
* d_j = requirement of nutrient j in the diet
* a_ij = content of nutrient j in food i
*
* min sum_i c_i x_i
* s.t. sum_i a_ij x_i >= d_j  for all j
* x_i >= 0 for all i
* ****************************************

SETS

i index of foods /apples,bananas,carrots,dates,eggs/
j index of nutrients /proteins,vitaminC,iron/
s(i) aaa /apples,bananas,carrots/;
PARAMETERS

d(j) requirement of nutrient j
         /proteins 70
          vitaminC 50
          iron 12/

c(i) cost of food i
         /apples 8
          bananas 10
          carrots 3
          dates 20
          eggs  15/;

TABLE a(i,j) content of nutrient j in food i
                    proteins   vitaminC   iron
         apples       0.4        6       0.4
         bananas      1.2       10       0.6
         carrots      0.6        3       0.4
         dates        0.6        1       0.2
         eggs         12.2       0       2.6;


VARIABLES
z        total cost of the diet
x(i)     units of food i in the diet;


POSITIVE VARIABLE x(i);


EQUATIONS
cost             the total diet cost
intake(j)        the intake of nutient j;


cost ..          z =e= sum((i), c(i)*x(i));
intake(j)..      sum(i,a(i,j)*x(i)) =g= d(j);



OPTION reslim = 1e10;
*OPTION limcol = 2;
OPTION limrow = 2;

MODEL diet /all/;
SOLVE diet USING lp MINIMIZING z;


DISPLAY
         x.l
         z.l
;

