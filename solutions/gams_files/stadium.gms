* ****************************************
* Implementation of the Stadium Construction Problem
* Giovanni Pantuso gp@math.ku.dk
* ****************************************

SET tasks 'The set of tasks' /1*18/;
alias(tasks,t1);
alias(tasks,t2);
SET precedences(tasks,tasks) 'The set precedences' /2.1,
					            3.2,
						    4.2,
						    5.3,
						    6.4,
						    6.5,
						    7.4,
						    8.6,
						    9.4,
						    9.6,
						    10.4,
						    11.6,
						    12.9,
						    13.7,
						    14.2,
						    15.4,
						    15.14,
						    16.8,
						    16.11,
						    16.14,
						    17.12,
						    18.17/;


PARAMETERS
duration(tasks) 'Duration of tasks in weeks'
         /1  2
	  2  16
	  3  9
	  4  8
	  5  10
	  6  6
	  7  2
	  8  2
	  9  9
	  10 5
	  11 3
	  12 2
	  13 1
	  14 7
	  15 4
	  16 3
	  17 9
	  18 1
	  /
	  ;


VARIABLES
z                'total duration'
t 		  'latest completion'
x(tasks)         'completion of a task'
;


POSITIVE VARIABLES
x(tasks)
t
;


EQUATIONS
totalduration                     'the expression of the total duration'
complete(tasks)     'completion after all tasks are done'
minduration(tasks)     'min duration'
actualduration(tasks,tasks)            'actual duration'
;




totalduration..       z =e= t;
complete(tasks)..      t =g= x(tasks);
minduration(tasks)..      x(tasks) =g= duration(tasks);
actualduration(tasks,t2)$precedences(tasks,t2).. 	       x(t1) =g= x(t2) + duration(t1);

* Sets the maximum CPU time (in seconds)
* the solver can spend to solve the problem
OPTION reslim = 3600;

MODEL stadium /all/;
SOLVE stadium USING lp MINIMIZE z;

DISPLAY
         z.l
         x.l;

