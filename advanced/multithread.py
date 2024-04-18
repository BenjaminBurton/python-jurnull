# Advanced Topics: Advanced Python

# Multithreading:

# Multithreading allows concurrent execution of multiple threads within a single process. Python's threading module provides a high-level interface for working with threads.

# Example: Multithreading with threading module
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()
