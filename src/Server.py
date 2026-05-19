import socket


# Server setup

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(('localhost', 6789))
s_socket.listen(5) # Listen for incoming connections (max of 5)

print("Waiting for a connection...")
connection, address = s_socket.accept()

# Receive data from client
data = connection.recv(1024)
print(f"Received message: {data.decode()} from {address}")

# Send a response to client
response = "Hello, client. Your message was receieved."
connection.send(response.encode())

connection.close()
