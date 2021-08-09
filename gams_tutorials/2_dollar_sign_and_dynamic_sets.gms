$Title  Examples
$Ontext
This file shows some examples on on how to use the dollar sign operator
$Offtext
$offlisting

********************************************************************
* First we generate some sets and parameters
* which we use to illustrate dollar sign and dynamic sets features
********************************************************************

SETS

i index of foods /apples,bananas,carrots,dates,eggs/
j index of nutrients /proteins,vitaminC,iron/

* Creates a subset of the foods
someFoods(i) subset of i /apples,bananas,carrots/;

****************************************************************

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


**************************************************************************
* Creates some parameters used to illustrate
* conditional assignment (Section 11, GAMS User Guide)
**************************************************************************

PARAMETERS
c1(i)   another version of costs
         /apples 8
          bananas 10
          carrots 3
          dates 20
          eggs  15/

c2(i)   another version of costs
         /apples 8
          bananas 10
          carrots 3
          dates 20
          eggs  15/

protein_sum
;

***********************************************
* The dollar sign operator is used as
* $(condition)
* It can be read as "such that 
* the condition in parentheses is true"
************************************************

**************************************************************************
* From the User Guide:
* For an assignment statement with a dollar condition on the left-hand side,
* no assignment is made unless the logical condition is satisfied.
* This means that the previous contents of the parameter on the left will remain
* unchanged for labels that do not satisfy the condition.
**************************************************************************
* In this case we add 1000 only the value of the elements in someFoods

c1(i)$someFoods(i) = c(i)+10000;
DISPLAY c1;

* Notice that subsets evaluate in Yes if the element is part of the
* subset, No otherwise, thus are treated as boolean variables

*******************************************************************
* From the User Guide:
* For an assignment statement with a dollar condition on the right hand side,
* an assignment is always made. If the logical condition is not satisfied,
* the corresponding term that the logical dollar condition is operating on evaluates to 0.
**************************************************************************
* In this case we add 10000 to the values corresponding to someFoods
* and set the others to 0
c2(i) = (c(i)+10000)$someFoods(i);
DISPLAY c2;


*************************************
* Sum of protein values in a(i,j)
*************************************

* Here I create a subset of I x J which contains
* only the pairs including proteins

SET proteins(i,j)
/
(apples,bananas,carrots,dates,eggs).proteins
/;

* Now I sum over the i,j of the table a(i,j) but
* considering only the i,j including proteins

protein_sum = sum((i,j)$proteins(i,j),a(i,j))
DISPLAY protein_sum;
DISPLAY proteins;


********************************************************************
* From the User Guide Chapter 12:
* A set whose membership can change is called a dynamic set to
* contrast it with a static set whose membership will never change.
********************************************************************

*************************************
* A simple example with dynamic sets
*************************************

SET dynamicFoods(i);

* Now it contains only apples
dynamicFoods('apples') = YES;
DISPLAY dynamicFoods;

* Now it contains everything
dynamicFoods(i) = YES;
DISPLAY dynamicFoods;

* Now we remove apples
dynamicFoods('apples') = NO;
DISPLAY dynamicFoods;

SET dynamicValues(i,j);

* Now it contains only combinations with apples
dynamicValues('apples',j) = YES;
DISPLAY dynamicValues;

* Now it is empty
dynamicValues(i,j) = NO;
DISPLAY dynamicValues;

* Now it contains only combinations with iron
dynamicValues(i,'iron') = YES;
DISPLAY dynamicValues;

