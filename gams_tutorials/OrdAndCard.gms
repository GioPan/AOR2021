* ****************************************
* Some examples with ord and card
* Giovanni Pantuso gp@math.ku.dk
* ****************************************
$onuellist
SETS

i index of fabric type /plain,patterned/
j index of production input /wool,loom,finishing/;

******************************************
* In this example we get the order of the
* elements in i and j.
* Remember that only static sets are ordered
* One note of warning: GAMS keeps a global
* list of UNIQUE elements. What does it mean?
* It means that if a member of a set appears
* in one or more sets, it is included only
* once in the global list. GAMS assigns the
* order to an element depending on where it
* appears in this list. As an example if you first
* define a set with elements A, B , C, and then you
* define another set with elements K, B, L,
* you might expect that the order of K is
* smaller than that of B (that it preceedes B)
* but it is actually not so. B is defined in the
* first set, and thus B preceedes K.
* As a rule of thumb, if the labels in a set
* one wants to be ordered have not been used
* already, then they will be ordered
* See Chapter 13.
******************************************

PARAMETERS
ordFabric(i) the order of the elements in i
ordInput(j) the order of the elements in j;

ordFabric(i) = ord(i);
ordInput(j) = ord(j);

DISPLAY ordFabric;
DISPLAY ordInput;

******************************************
* Some operations on matrices
******************************************

SET r row and column labels / 1*5 /;
alias (r,c);

* e(r,c) will contain the matrix
PARAMETER e(r,c) a general square matrix;

* e is now an upper triangular matrix
e(r,c)$(ord(r) le ord(c)) = ord(r) + ord(c) ;
DISPLAY e;

* e is now a diagonal matrix (remember assignement with
* dollar condition on the right-hand side)
e(r,c) = (ord(r) + ord(c))$(ord(r) eq ord(c)) ;
DISPLAY e;

* e is now a lower triangular matrix
e(r,c)$(ord(r) ge ord(c)) = ord(r) + ord(c) ;
DISPLAY e;

* e is now a strictly upper triangular matrix
e(r,c) = (ord(r) + ord(c))$(ord(r) lt ord(c)) ;
DISPLAY e;

* e is now a strictly lower triangular matrix
e(r,c) = (ord(r) + ord(c))$(ord(r) gt ord(c)) ;
DISPLAY e;

PARAMETER f(r);

* Only the last element of f will get a value
f(r)$(ord(r) = card(r)) = 100 ;
DISPLAY f;

* Now also the second-last element of f will get a value
f(r)$(ord(r) eq card(r)-1) = 100 ;
DISPLAY f;

* Now only the second-last element of f will get a value
f(r) = 100$(ord(r) eq card(r)-1) ;
DISPLAY f;






