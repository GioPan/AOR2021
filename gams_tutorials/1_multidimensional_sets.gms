$Title  Examples
$Ontext
This file shows some examples on on how to use multidimensional sets.
Further details are provided at https://www.gams.com/latest/docs/UG_DataEntry.html#UG_DataEntry_Parameters.
$Offtext
$offlisting

* We create some sets which we use to building multidimensional parameters
SETS
A 'Set A' /a1*a5/
B 'Set B' /b1*b3/
C 'Set C' /c1,c2/
;


* The following parameter has three dimensions, A, B and C.
* To create such parameter we pass each tuple with the element separated by a dot.
* The tuples for which we do not pass a value get automatically a 0.
PARAMETERS

cost(A,B,C) 'The cost of a tuple (a,b,c)'
/a1.b1.c1 = 10
 a1.b2.c1 = 20
 a1.b3.c1 = 30
 a3.b2.c2 = 9
 /

* Repeated elements can be placed in parentheses.
* In what follows both (a1,b1,c1) and (a3,b1,c1) will have the same value.
* Furthermore, it is possible to use the asterisk to capture lists of values.
* In the example, all tuples starting with a2, a3, a4 or a5 followed by b2 and c1 are initialized
* with the value 10.
price(A,B,C) 'The price of a tuple (a,b,c)'
/(a1,a3)  .b1 .c1 = 7
 a2*a5 .b2 . c1 = 10
 a1*a3. b1*b2.c2 = 15/
;
DISPLAY
cost
price
;