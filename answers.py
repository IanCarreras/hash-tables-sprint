1) A hashing function is any function that generates a value from 
a string of text.  A specified input will always return the same
hash value.  A hash value can be the same for two different inputs

2) Collision resolution is solving the problem of equal hash values 
from different inputs

3) Performance of basic hash table operations

4) Load factor is a measure of how full the hash table is.  The load 
factor is calculated by divided the number of items in the table by
the capacity of the table

5)  Automatic resizing is increasing or decreasing the capacity of 
the hash table based on the load factor.  Best practice is to 
increase by double and decrease by half because resizing is a computationally
expense operation.  

6) A hash table is used to make retrieving values a less time expensive
operation
