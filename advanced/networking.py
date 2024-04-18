# Advanced Topics: Advanced Python

# 3.6.3 Networking:

# Python provides several modules for networking, such as socket for low-level networking, http.server for building HTTP servers, and third-party libraries like requests for making HTTP requests.

# Example: Networking with socket module
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
server_socket.bind(('127.0.0.1', 12345))

# Listen for incoming connections
server_socket.listen(5)

# Accept connections from clients
client_socket, address = server_socket.accept()

# Receive data from the client
data = client_socket.recv(1024)
print("Received:", data.decode())

# Close the sockets
client_socket.close()
server_socket.close()

# Practice, Practice, PRACTICE