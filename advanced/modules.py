# 3.1 Modules and Packages: Advanced Python

# Modules and Packages:

# Modules:

# Modules in Python are simply Python files containing definitions and statements. You can import modules into your scripts to use their functionality.

# Example: Importing Modules
import math
print(math.sqrt(25)) # Output: 5.0



# Packages:

# Packages are namespaces that contain multiple modules. They are directories with a special __init__.py file.

# Example: Importing from Packages
# Assuming we have a package named 'my_package' with a module named 'my_module' inside it.
from my_package import my_module
my_module.my_function()


# Creating Your Own Modules and Packages:

# You can create your own modules and packages by organizing your code into separate Python files and directories.

# Example: Creating a Module
# Save this code in a file named my_module.py
def my_function():
    print("This is my function in my_module")

# Example: Creating a Package
# Create a directory named 'my_package' with an empty '__init__.py' file inside it.
# Inside 'my_package', create a file named 'my_module.py' with the content of the previous example.
