import socket

# Server setup
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_socket.bind(('localhost', 6789))

# Send a message to the server
message = "Hello, server!"
c_socket.send(message.encode())

# Receiving response from server
response = c_socket.recv(1024)
print(f"Received from server: {response.decode()}")

c_socket.close()