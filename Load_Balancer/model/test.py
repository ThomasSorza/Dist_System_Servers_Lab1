import socket
import threading
from main_server import Server

MAX_CLIENTS = 1
PORT = 446

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)  # Recibe datos del cliente

            if not data:
                break  # Si no se recibe ningún dato, el cliente se ha desconectado

            message = data.decode('utf-8')  # Convierte los bytes recibidos a una cadena
            response = f"Received: {message}"
            client_socket.send(response.encode('utf-8'))  # Envía una respuesta de vuelta al cliente

    except Exception as e:
        print(f"Error while handling client: {e}")

    finally:
        client_socket.close()  # Cierra el socket del cliente cuando termina

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', PORT))
    server_socket.listen(5)

    print(f"Server listening on port {PORT}...")

    # Lista para mantener las conexiones activas
    active_clients = []

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from: {client_address}")

            # Verifica si se ha alcanzado el límite máximo de clientes
            if len(active_clients) < MAX_CLIENTS:
                active_clients.append(client_socket)
                threading.Thread(target=handle_client, args=(client_socket,)).start()
            else:
                print("Maximum number of customers reached. Putting the customer on hold.")
                

        except KeyboardInterrupt:
            print("Server shutting down.")
            break

if __name__ == "__main__":
    main()