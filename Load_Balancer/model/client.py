import socket
import time

def main():
    host = '127.0.0.1'  # Server's IP address or hostname
    port = 446         # Server's port

    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print("Connected to the server.")

            try:
                while True:
                    message = input("Enter a message (or 'exit' to quit): ")
                    
                    if message.lower() == 'exit':
                        break  # Exit the loop if the user types 'exit'
                    
                    client_socket.send(message.encode('utf-8'))
                    response = client_socket.recv(1024).decode('utf-8')
                    print("Server:", response)

            except KeyboardInterrupt:
                print("\nKeyboard Interrupt. Closing client...")
                break

            finally:
                client_socket.close()

        except (ConnectionError, ConnectionAbortedError, ConnectionResetError):
            print("Connection to the server lost. Reconnecting...")
            try:
                time.sleep(2)  # Wait for a short period before attempting to reconnect
            except KeyboardInterrupt:
                    print("\nKeyboard Interrupt. Closing client...")
                    break

if __name__ == "__main__":
    main()
