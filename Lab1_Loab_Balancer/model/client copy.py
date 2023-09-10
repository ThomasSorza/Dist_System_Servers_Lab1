import socket
import time

def main():
    host = '127.0.0.1'  # Server's IP address or hostname
    port = 447      # Server's port
    tries = 0      

    while tries < 5:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print("Connected to the server.")

            try:
                while True:
                    message = input("Enter a message (or 'exit' to quit): ")
                    
                    if message.lower() == 'exit':
                        client_socket.send(message.encode('utf-8'))
                        client_socket.close()
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
            try:
                time.sleep(1)  # Wait for a short period before attempting to reconnect
                tries += 1
            except KeyboardInterrupt:
                    print("\nKeyboard Interrupt. Closing client...")
                    break
    print("Connection to the server lost. Closing client...")

if __name__ == "__main__":
    main()