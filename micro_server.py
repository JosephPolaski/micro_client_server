"""
Sources Cited:
Title: Python Socket Programming Tutorial
Author: Tech With Tim
URL: https://www.youtube.com/watch?v=3QiPPX-KeSc&t=2593s
Description: We followed this tutorial and used/refactored the code into our
own implementation to build the server as a prtable class.

Sources Cited:
Title: Sockets Tutorial with Python 3 part 3 - sending and receiving Python Objects w/ Pickle
Author: HSKinsley (Sentdex)
URL: https://www.youtube.com/c/sentdex/about
Description: We followed this tutorial and used it as a reference for using
pickling with python sockets
"""
import socket
import pickle

class micro_server:
    
    self.__init__(self, call_back):
        self.__HEAD = 64 # header of 64 bytes for message protocol 
        self.__PORT = 5467
        self.__IP = socket.gethostbyname(socket.gethostname())
        self.__socket = self.define_micro_socket()
        self.__disconnect_msg = "&END"
        self.__call_back = call_back # call back function to process request
        self.start_listening()     
     
    def define_micro_socket(self):
        """Create and bind socket to port 5467"""
        micro_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        micro_socket.bind(self.__IP, self.__Port)) 
        return micro_socket

    def start_listening(self):
        """continuously listen for connections"""
        self.__socket.listen(100)
        while True:
            # blocks until connection to socket is detected
            client, address = self.__socket.accept()
            handle_client_requests(client, address)

    def handle_client_requests(self, client, address):
        print(f"New Connection from {address}")

        connected = True
        while connected:
            # fetch length of incoming message from header
            data_length = self.get_data_length()

            # fetch incoming request
            request = self.get_actual_data(data_length) 

            client.close() if request == self.__disconnect_msg else self.__call_back(request)           
    
    def get_data_length(self):
        """helper to handle_client_requests()"""
        # blocks until request header recieved
        data_length = client.recv(self.__HEAD).decode('utf-8')

        # cast decoded header as integer length
        data_length = int(data_length)

        return data_length 
    
    def get_actual_data(self, data_length):
         """helper to handle_client_requests()"""
        # blocks until request data recieved
        request = client.recv(data_length).decode('utf-8')    
        return request
        

    


