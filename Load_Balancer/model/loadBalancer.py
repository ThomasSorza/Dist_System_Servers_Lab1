import threading

from server import ServerTCP as Server

MAX_CLIENTS = 5
PORT = 446
queue_clients = []

# get the next client in the queue
def getNextClient():
    return queue_clients.pop(0)

#check if there are clients waiting in the queue
def areClientsWaiting():
    return len(queue_clients) > 0

# Handle messages from a client socket
def handle_client(client_socket, server):
    try:
        while True:
            data = client_socket.recv(1024)  # Receive data from the client
            if not data:
                break  # If no data received, the client has disconnected
            message = data.decode('utf-8')  # Convert the received bytes to a string
            if(message == "exit"): # If the client sends 'exit', close the connection
                client_socket.close()
                print(f"Connection ended from: {client_socket}")
                server.getUsersConnected().remove(client_socket)
                print(f"Number of clients connected: {len(server.getUsersConnected())}")
                break
            response = f"Received: {message}"
            client_socket.send(response.encode('utf-8'))  # Send a response back to the client
            print(f"Message from client: {message}")

    except Exception as e:
        print(f"Error while handling client: {e}")

    finally:
        client_socket.close()  # Close the client socket when done

#start the load balancer
def start(): 
    mainServer = Server(446, 3)
    slave = Server(447, 3)
    slave.bind()
    mainServer.bind()
    #start the main server
    mainServer.startListening()
    print(f"Server listening on port {mainServer}...")

    while True:
        if not mainServer.isFull():
            # Accept a new connection and handle messages from the client
            try:
                if not areClientsWaiting():
                    client_socket, client_address = mainServer.accept()
                    mainServer.getUsersConnected().append(client_socket)
                    print(f"Connection from: {client_address}")
                    client_socket.send("You are connected to the server 1.".encode('utf-8'))
                    # Start a new thread to handle the client connection
                    server1thread = threading.Thread(target=handle_client, args=(client_socket, mainServer,))
                    server1thread.start()
                else:
                    client_socket = getNextClient()
                    mainServer.getUsersConnected().append(client_socket)
                    print(f"Connection from: {client_address}")
                    client_socket.send("You are connected to the server 1.".encode('utf-8'))
                    # Start a new thread to handle the client connection
                    server1thread = threading.Thread(target=handle_client, args=(client_socket, mainServer,))
                    server1thread.start()

            except KeyboardInterrupt:
                print("Server shutting down.")
                break

        #start the slave server if the main server is full and the slave is not listening yet
        elif(mainServer.isFull() and not slave.getIsListening()):
            slave.startListening()
            print(f"Slave Server listening on port {slave}...")

        #if the main server is full and the slave is listening, put the client in the slave server
        elif(mainServer.isFull() and not slave.isFull() and slave.getIsListening()):
            try:
                if not areClientsWaiting():
                    client_socket, client_address = slave.accept()
                    slave.getUsersConnected().append(client_socket)
                    print(f"Connection from: {client_address}")
                    client_socket.send("You are connected to the server 2.".encode('utf-8'))
                    # Start a new thread to handle the client connection
                    server2thread = threading.Thread(target=handle_client, args=(client_socket,))
                    server2thread.start()
                else:
                    client_socket = getNextClient()
                    slave.getUsersConnected().append(client_socket)
                    print(f"Connection from: {client_address}")
                    client_socket.send("You are connected to the server 2.".encode('utf-8'))
                    # Start a new thread to handle the client connection
                    server2thread = threading.Thread(target=handle_client, args=(client_socket,))
                    server2thread.start()

            except KeyboardInterrupt:
                print("Server shutting down.") #shut down the server
                break

        #if both servers are full, put the client in the queue
        elif(mainServer.isFull() and slave.isFull()):
            client_socket, client_address = mainServer.accept()
            queue_clients.append(client_socket)
            client_socket.send("We are busy now. You are in the queue.".encode('utf-8'))
            break

if __name__ == "__main__":
    start()