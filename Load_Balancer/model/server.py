import socket
import re

#Server class
class Server(socket.socket):

    #server constructor method as INET ipv4 and TCP socket
    def __init__(self,port, max_clients, host = 'localhost', users_connected = []):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.max_clients = max_clients
        self.host = host
        self.users_connected = users_connected

    """
    Getter and Setter methods
    """
    # Getter and Setter methods for port
    def getPort(self):
        return self.port

    def setPort(self, new_port):
        self.port = new_port

    # Getter and Setter methods for max_clients
    def getCapacity(self):
        return self.max_clients

    def setCapacity(self, new_max_clients):
        self.max_clients = new_max_clients

    # Getter and Setter methods for host
    def getHost(self):
        return self.host

    def setHost(self, new_host):
        if self.is_ipv4(new_host):
            self.host = new_host
    
    # Getter and Setter methods for users_connected
    def getUsersConnected(self):
        return self.users_connected
    
    def setUsersConnected(self, new_users_connected):
        self.users_connected = new_users_connected

    # Bind the socket to the host and port from attributes
    def bind(self):
        super().bind((self.host, self.port))
    
    # Listen for max_clients connections
    def startListening(self):
        super().listen(self.max_clients)

    # Check if the server is full
    def isFull(self):
        return len(self.users_connected) >= self.max_clients

    #check if the ip is valid (ipv4)
    @staticmethod
    def is_ipv4(new_ip):
        valid_id = False
        ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$' # Regular expression for matching IPv4 addresses
        if re.match(ipv4_pattern, new_ip):  # Use the re.match() function to check the pattern
            valid_id = True
        return valid_id

    def __str__(self):
        return f"Server (Host: {self.host}, Port: {self.port}, Max Clients: {self.max_clients})"
