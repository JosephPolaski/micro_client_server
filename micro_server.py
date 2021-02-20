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
    
    def __init__(self, call_back):
        self.define_data_members(call_back)
        self.start_listening()

    def define_data_members(self, call_back):
        self.define_address_members()

        # define end protocol, call back function and socket
        self.__DCON = "&END"
        self.__call_back = call_back
        self.__socket = self.define_micro_socket()
    
    def define_address_members(self):
        self.__HEAD = 64  # header of 64 bytes for message protocol
        self.__PORT = 5467
        self.__IP = socket.gethostbyname(socket.gethostname())
        self.__ADDR = (self.__IP, self.__PORT)
    
    def define_micro_socket(self):
        """Create and bind socket to port 5467"""
        micro_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        micro_socket.bind(self.__ADDR)
        return micro_socket

    def start_listening(self):
        """continuously listen for connections"""
        self.__socket.listen(100)
        while True:
            # blocks until connection to socket is detected
            client, address = self.__socket.accept()
            request = self.handle_client_requests(client, address)

            # check for closing request
            client.close() if request == self.__DCON else self.__call_back(request)

    def handle_client_requests(self, client, address):
        print(f"New Connection from {address}")
        
        connected = True
        while connected:
            # fetch length of incoming message from header
            data_length = self.get_data_length(client)
           
            # fetch incoming request
            request = self.get_actual_data(client, data_length)
            return request            

    def get_data_length(self, client):
        """helper to handle_client_requests()"""
        # blocks until request header recieved
        data_length = client.recv(self.__HEAD).decode('utf-8')
        
        # cast decoded header as integer length
        data_length_int = int(data_length)     
        
        return data_length_int

    def get_actual_data(self, client, data_length):
        """helper to handle_client_requests()"""
        # blocks until request data recieved
        request = client.recv(data_length).decode('utf-8')        
        return request

# main function for test
if __name__ == "__main__":

    # test callback function
    def call_back(request):
        print(f'request is {request}')

    server = micro_server(call_back)


    


