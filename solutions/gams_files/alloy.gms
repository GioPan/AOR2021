* ****************************************
* Implementation of the Alloy Production Problem
* Giovanni Pantuso gp@math.ku.dk
* ****************************************

SET chemicals 'The chemicals to trace in the alloy' /carbon,copper,manganese/;
SET raw 'The set of raw materials' /iron1,iron2,iron3,copper1,copper2,allum1,allum2/;


SCALAR
D 'Demand' /500/
;

PARAMETERS
mingrade(chemicals) 'Min grade in the final alloy (percentage)'
         /carbon 2.0
         copper  0.4
         manganese 1.2/


maxgrade(chemicals) 'Max grade in the final alloy (percentage)'
         /carbon 3.0
         copper  0.6
         manganese 1.65/

availability(raw) 'Amount available of raw material (tonnes)'
/
iron1     400
iron2     300
iron3     600
copper1   500
copper2   200
allum1    300
allum2	  250
/

cost(raw) 'Cost of raw material (Euro/tonne)'
/
iron1     200
iron2     250
iron3     150
copper1   220
copper2   240
allum1    200
allum2	  165
/	
;


TABLE content(raw,chemicals) 'Content of chemicals in the raw materials (percentage)'
         carbon copper manganese      			  
iron1     2.5     0.0   1.3
iron2     3.0     0.0   0.8
iron3     0.0     0.3   0.0
copper1   0.0     90.0  0.0
copper2   0.0     96.0  4.0
allum1    0.0	  0.4	1.2
allum2	  0.0	  0.6	0.0
;



VARIABLES
z                'total cost'
x(raw)         'amount of raw material used in the alloy'
;


POSITIVE VARIABLES
x(raw)
;


EQUATIONS
totalcost                     'the expression of the total cost'
ming(chemicals)     'min grade'
maxg(chemicals)     'max grade'
avail(raw)            'availability'
dem              'demand constraint'
;


* Check out how to write summations on the User Guide

totalcost..       z =e= sum(raw, cost(raw)*x(raw));


ming(chemicals)..      sum(raw,content(raw,chemicals) * x(raw)) =g= mingrade(chemicals) * sum(raw,x(raw));
maxg(chemicals)..      sum(raw,content(raw,chemicals) * x(raw)) =l= maxgrade(chemicals) * sum(raw,x(raw));
avail(raw).. 	       x(raw) =l= availability(raw);
dem..		       sum(raw,x(raw)) =g= D;

* Sets the maximum CPU time (in seconds)
* the solver can spend to solve the problem
OPTION reslim = 3600;

MODEL alloy /all/;
SOLVE alloy USING lp MINIMIZE z;

DISPLAY
         z.l
         x.l;

