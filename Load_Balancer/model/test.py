import socket
import threading
from server import Server

MAX_CLIENTS = 5
PORT = 446

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)  # Receive data from the client

            if not data:
                break  # If no data received, the client has disconnected

            message = data.decode('utf-8')  # Convert the received bytes to a string
            response = f"Received: {message}"
            client_socket.send(response.encode('utf-8'))  # Send a response back to the client

    except Exception as e:
        print(f"Error while handling client: {e}")

    finally:
        client_socket.close()  # Close the client socket when done

def main():
    server = Server(446, 8)
    server.bind()
    server.startListening()

    print(f"Server listening on port {server}...")

    while True:
        try:
            client_socket, client_address = server.accept()
            print(f"Connection from: {client_address}")

            # Start a new thread to handle the client connection
            threading.Thread(target=handle_client, args=(client_socket,)).start()

        except KeyboardInterrupt:
            print("Server shutting down.")
            break

if __name__ == "__main__":
    main()
