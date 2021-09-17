* ****************************************
* Implementation of the Stadium Construction Problem
* Giovanni Pantuso gp@math.ku.dk
* ****************************************

SET blocks 'The set of blocks' /1*18/;
alias(blocks,b1);
alias(blocks,b2);
SET precedences(blocks,blocks) 'The set precedences'
						   /9.1,
					            9.2,
						    9.3,
						    10.2,
						    10.3,
						    10.4,
						    11.3,
						    11.4,
						    11.5,
						    12.4,
						    12.5,
						    12.6,
						    13.5,
						    13.6,
						    13.7,
						    14.6,
						    14.7,
						    14.8,
						    15.9,
						    15.10,
						    15.11,
						    16.10,
						    16.11,
						    16.12,
						    17.11,
						    17.12,
						    17.13,
						    18.12,
						    18.13,
						    18.14/;


PARAMETERS
cost(blocks) 'Cost of mining each block'
	     /1 100
             2  100
	     3  100
	     4  100
	     5  100
	     6  100
	     7  100
	     8  100
	     9  1000
	     10  200
	     11  200
	     12  200
	     13  200
	     14  1000
	     15  1000
	     16  1000
	     17  300
	     18  1000/

value(blocks) 'Value of mining each block'
	     /1 200
             2  0
	     3  0
	     4  0
	     5  0
	     6  0
	     7  300
	     8  0
	     9  0
	     10  500
	     11  0
	     12  200
	     13  0
	     14  0
	     15  0
	     16  0
	     17  1000
	     18  1200/
	     ;

VARIABLES
z                'total profit'
x(blocks)         'mining of block'
;


BINARY VARIABLES
x(blocks)
;


EQUATIONS
profit                     'the expression of the total profit'
precedence(blocks, blocks)     'mining precedences'
;




profit..       z =e= sum(blocks, value(blocks) * x(blocks) - cost(blocks) * x(blocks));
precedence(b1,b2)$precedences(b1,b2).. 	       x(b1) =l= x(b2);

* Sets the maximum CPU time (in seconds)
* the solver can spend to solve the problem
OPTION reslim = 3600;

MODEL mining /all/;
SOLVE mining USING mip MAXIMIZE z;

DISPLAY
         z.l
         x.l;

