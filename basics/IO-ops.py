#  Input/Output Operations:

# Input from User:



# You can use the input() function to prompt the user for input. It reads input from the keyboard as a string.

# Example: Input from User
name = input("Enter your name: ")
print("Hello,", name)



# Output to Console:

# You can use the print() function to display output to the console. It can print strings, variables, and expressions.

# Example: Output to Console
x = 10
y = 20
print("The sum of", x, "and", y, "is", x + y)


# Reading and Writing Files:

# You can read from and write to files using Python's file handling capabilities.

# Example: Reading and Writing Files
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a text file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)


