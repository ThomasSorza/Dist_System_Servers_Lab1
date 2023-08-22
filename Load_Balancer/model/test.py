import socket
import threading
from server import Server
import time

MAX_CLIENTS = 5
PORT = 446
queue_clients = []

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)  # Receive data from the client
            if not data:
                break  # If no data received, the client has disconnected
            message = data.decode('utf-8')  # Convert the received bytes to a string
            response = f"Received: {message}"
            client_socket.send(response.encode('utf-8'))  # Send a response back to the client
            print(f"Message from client: {message}")

    except Exception as e:
        print(f"Error while handling client: {e}")

    finally:
        client_socket.close()  # Close the client socket when done

def main():
    server = Server(446, 2)
    server.bind()
    server.startListening()
    print(f"Server listening on port {server}...")

    while True:
        if(len(server.getUsersConnected()) < server.getCapacity()):
            try:
                client_socket, client_address = server.accept()
                server.getUsersConnected().append(client_socket)
                print(f"Connection from: {client_address}")
                print(f"Clients connected en server1: {len(server.getUsersConnected())}")
                # Start a new thread to handle the client connection
                server1thread = threading.Thread(target=handle_client, args=(client_socket,))
                server1thread.start()
                

            except KeyboardInterrupt:
                print("Server shutting down.")
                break
        else:
            print("Server full")
            break

if __name__ == "__main__":
    main()