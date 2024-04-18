# Data Science and Machine Learning: Advanced Python

# 3.5.2 Pandas:

# Pandas is a powerful library for data manipulation and analysis in Python. It provides data structures like Series and DataFrame, which are designed to handle labeled and relational data easily.

# Example: Using Pandas
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [30, 25, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
