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
    server2 = Server(445, 2)
    server.bind()
    server.startListening()
    print(f"Server listening on port {server}...")

    while True:
        if(not server.isFull()):
            try:
                client_socket, client_address = server.accept()
                server.getUsersConnected().append(client_socket)
                print(f"Connection from: {client_address}")
                client_socket.send("You are connected to the server.".encode('utf-8'))
                # Start a new thread to handle the client connection
                server1thread = threading.Thread(target=handle_client, args=(client_socket,))
                server1thread.start()

            except KeyboardInterrupt:
                print("Server shutting down.")
                break
        #elif(#is not up):
            #start server2
        elif(server.isFull() and not server2.isFull()):
            try:
                # Encolar al cliente en el server 2
                queue_clients.append(client_socket)
                print("Server full, adding client to the queue.")
                # Notificar al cliente que está en espera
                client_socket.send("Server is full.".encode('utf-8'))
            except:
                print("Server full")
                break

if __name__ == "__main__":
    main()