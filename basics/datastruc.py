# Data structure basics

# Lists : Lists are ordered collections of items, and they can contain elements of different data types.


# Example : List

my_list = [1, 2, 3, 4, 5]                           # Create a list

print(my_list)                                      # Output : [1, 2, 3, 4, 5]



# Accessing Elements 

print(my_list[0])                                   # Output : 1 (Indexing starts from 0)

print(my_list[-1])                                  # Output : 5 (Negative indexing starts from the end)



# Slicing 

print(my_list[1:4])                                 # Output : [2, 3, 4] (Slice from index 1 to 3)




# Tuples : Tuples are ordered collectionsof items, similar to lists, but they are immutable (cannot be modified)


# Example : Tuples

my_tuple = (1, 2, 3)                                # Create a tuple

print(my_tuple)                                     # Output : (1, 2, 3)



# Accessing Elements

print(my_tuple[0])                                  # Output : 1




# Dictionaries : Dictionaries are unordered collections of key-value pairs.

# Example: Dictionaries
my_dict = {"name": "John", "age": 30, "city": "New York"} # Create a dictionary
print(my_dict)                                      # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements
print(my_dict["name"])                              # Output: John

# Adding or updating elements
my_dict["email"] = "john@example.com"
print(my_dict)                                      # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}




# Sets: Sets are unordered collections of unique elements.

# Example: Sets
my_set = {1, 2, 3, 4, 5} # Create a set
print(my_set)            # Output: {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)            # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(3)
print(my_set)            # Output: {1, 2, 4, 5, 6}

