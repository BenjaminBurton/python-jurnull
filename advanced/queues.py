# 3.2.2 Advanced Data Structures: Advanced Python

# Queues:

# A queue is a collection of elements that follows the First In, First Out (FIFO) principle. You can use the queue module in Python to implement a queue.

# Example: Queue Implementation using queue.Queue
from queue import Queue

# Create a queue
queue = Queue()

# Enqueue elements
queue.put(1)
queue.put(2)
queue.put(3)

# Dequeue elements
print(queue.get()) # Output: 1
