# Exception Handling: Intermediate Python

# Handling Exceptions:

# You can use try and except blocks to handle exceptions (errors) gracefully in Python.

# Example: Handling Exceptions
try:
    x = 10 / 0 # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero")



# Handling Multiple Exceptions:

# You can handle multiple types of exceptions in a single try block.

# Example: Handling Multiple Exceptions
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero")



# Finally Block:

# You can use a finally block to execute cleanup code regardless of whether an exception occurs or not.

# Example: Finally Block
try:
    file = open("example.txt", "r")
    contents = file.read()
    print(contents)
except FileNotFoundError:
    print("Error: File not found")
finally:
    if 'file' in locals():
        file.close()