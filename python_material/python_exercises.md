# Exercise 1
Complete the following function such that it returns a dictionary which associates a number of each letter of the alphabet.
As an example, it associates $1$ to A, $2$ to B and so on.
```python
def get_alphabet_dictionary():
    d = {'A':1,'B':2}
    return d
```
# Exercise 2
Using the function written above complete the following function such that
it receives a string as an argument and prints a numerical code obtained by replacing the letters of the string with their
numerical value.
```python
def get_code(s:str):  
      
```

# Exercise 3
Using the function `get_alphabeth_dictionary` written above complete the following function such that
it receives a string as an argument and returns a list which contains the numerical code of each letter of the string passed.
As an example, if we pass "ABC" it must return `[1,2,3]`. Use list comprehension.
```python
def get_code_list(s:str):
    l = []
    # populate the list 
    return l  
```

# Exercise 4
Complete the following function such that, given a dictionary similar to that of Exercise 1, 
it returns a dictionary with the numerical values raised to the power of 2.
As an example, if the argument dictionary is `d1 = {'A': 3,'B': 2}` it must return `d2 = {'A':9,'B':4}`.
```python
def get_squared_codes(d:dict):
    """
    Given a dictionary which contains, for each key, a numerical value (similar to the one in exercise 1) 
    creates and returns a similar dictionary but such that the numerical value is squared.
    :return: dict
    """
    squared_dict = {l : d[l] ** 2 for l in d}
    return squared_dict
```

# Exercise 5
Consider a network consisting of $N$ nodes. There are arcs for each pair of nodes. 
There is no arc between the node and itself, e.g., no arc from $3$ to $3$.
Complete the following function in order to return the list of arcs, given the number of nodes. 
Each arc must be represented as a tuple.
```python
def generate_arcs(n_nodes:int):
    '''
    Generates and returns the list of arcs as tuples.
    '''
``` 

# Exercise 6
Consider a network consisting of $N$ nodes. There are arcs only between the nodes that are both odd or both even. 
For example, there will be an arc between $1$ and $3$, an arc between $2$ and $4$, but not between $1$ and $2$. 
Also, there is no arc between the node and itself, e.g., no arc from $3$ to $3$.
Complete the following function in order to return the list of arcs, given the number of nodes. 
Each arc must be represented as a tuple.
```python
def generate_arcs(n_nodes:int):
    '''
    Generates and returns the list of arcs as tuples.
    '''
``` 

# Exercise 7

Complete the code below to write a class representing rectangles.
```python
class Rectangle:

    def __init__(self, length:float, height: float):
        '''
        Builds a rectangle given its length and height.
        '''

    def get_perimeter(self):
        '''
        :returns the perimeter of the rectangle
        '''
    
    def get_area(self):
        '''
        :returns the area of the rectangle
        '''

    def scale(self, scalar:float):
        '''
        Multiplies the dimensions of the rectangle by the scalar passed as an argument.
        '''
``` 

# Exercise 8

Complete the code below to write a class representing circles.
Pay particular attention at the constant $\pi$. How do you code it? 
```python
class Circle:

    def __init__(self, radius:float):
        '''
        Builds a circle given its radius.
        '''

    def get_circumference(self):
        '''
        :returns the circumference of the circle
        '''
    
    def get_area(self):
        '''
        :returns the area of the circle
        '''

    def scale(self, scalar:float):
        '''
        Multiplies the radius by the scalar passed as an argument.
        '''
``` 