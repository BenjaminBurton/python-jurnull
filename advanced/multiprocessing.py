# Advanced Topics: Advanced Python

# 3.6.2 Multiprocessing:

# Multiprocessing allows parallel execution of multiple processes, which can take advantage of multiple CPU cores. Python's multiprocessing module provides a similar interface to working with processes as the threading module does for threads.

# Example: Multiprocessing with multiprocessing module
import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# Create a process
process = multiprocessing.Process(target=print_numbers)

# Start the process
process.start()

# Wait for the process to finish
process.join()
