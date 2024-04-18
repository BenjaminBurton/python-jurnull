# 2.3 Functional Programming: Intermediate Python

# Lambda Functions:

# Lambda functions are small anonymous functions that can have any number of parameters but only one expression.

# Example: Lambda Functions
# Syntax: lambda parameters: expression
square = lambda x: x ** 2
print(square(5)) # Output: 25



# Map, Filter, and Reduce:

# map() applies a function to all the items in an iterable.

# filter() filters out items based on a condition.

# reduce() applies a rolling computation to sequential pairs of values in an iterable.

# Example: Map, Filter, and Reduce
# map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared) # Output: [1, 4, 9, 16, 25]

# filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4]

# reduce() (Python 3.x requires importing from functools)
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers) # Output: 15 (1 + 2 + 3 + 4 + 5)