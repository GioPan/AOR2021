* ****************************************
* EXAMPLE OF HOW TO READ DATA FROM A FILE
* Giovanni Pantuso gp@math.ku.dk
* ****************************************
* To remember: when reading from a file, the file content is
* assumed to be GAMS code. Thus, including a text file within
* a data statement allows for an easy way to include data from
* a text file, as long as the syntax in the text file can be
* understood by the GAMS compiler.

SETS

i index of columns /1*10/
j index of rows /1*20/
k another set /1*5/;

* We use the $include operator which takes as argument a data file where the
* data is stored. The data file must be formatted exactly as you would format
* the data directly in GAMS, that is:
*
* index1 value1
* index2 value2
* ...

PARAMETER
c(i) cost of column i /
$include read_cost.txt
/ ;

* For tables we use the structure
*        indexA   indexB ...
*index1  value1A  value1B ...
*index2  value2A  value2B ...

TABLE a(j,i) a matrix
$include read_matrix.txt
;


* We can also include parameters using the assignment of type
* b(k) = value;
* This is particularly useful for parameters with many indexes
* such as p(i,j,k,l,m)

PARAMETER b(k);
$include read_param.txt

DISPLAY
         c
         a
	 b;


