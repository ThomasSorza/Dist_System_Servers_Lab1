import socket
import time

def main():
    host = '127.0.0.1'  # Server's IP address or hostname
    port = 446         # Server's port
    tries = 0  # Initialize the number of connection attempts
    queued = False #TODO: implementar cola de espera

    while tries < 10:  # Continue loop as long as attempts are less than 10
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print("Connected to the server.")
            
            response = client_socket.recv(1024).decode('utf-8')
            print("Server:", response)

            if "Server is full." in response:
                print("Server is full. You are in the queue.")
                while True:
                    response = client_socket.recv(1024).decode('utf-8')
                    print("Server:", response)
                    if "You are next in line." in response:
                        print("You are next in line. Waiting for your turn...")
                        break
                    time.sleep(2)  # Wait before checking again

            try:
                while True:
                    message = input("Enter a message (or 'exit' to quit): ")
                    
                    if message.lower() == 'exit':
                        exit(0)  # Exit the loop if the user types 'exit'
                    
                    client_socket.send(message.encode('utf-8'))
                    response = client_socket.recv(1024).decode('utf-8')
                    print("Server:", response)

            except KeyboardInterrupt:
                print("\nKeyboard Interrupt. Closing client...")
                break

            finally:
                client_socket.close()

        except (ConnectionError, ConnectionAbortedError, ConnectionResetError):
            print("Connection to the server lost. Trying Reconnecting...")
            tries += 1
            time.sleep(2)  # Wait for a short period before attempting to reconnect

    print("Maximum number of connection attempts reached. Exiting...")

if __name__ == "__main__":
    main()
