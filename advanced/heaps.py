# 3.2.3 Advanced Data Structures: Advanced Python

# Heaps:

# A heap is a binary tree-based data structure that satisfies the heap property. You can use the heapq module in Python to implement a heap.

# Example: Heap Implementation using heapq
import heapq

# Create a list
heap = []

# Add elements to the heap
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# Remove elements from the heap
print(heapq.heappop(heap)) # Output: 1
