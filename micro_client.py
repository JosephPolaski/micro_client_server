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
Sources Cited:
Title: Socket Programming in Python using Pickle
Author: StackOverflow -- user: B Morris
URL: https://stackoverflow.com/questions/53576851/socket-programming-in-python-using-pickle
Description: I followed this method for sending pickled data over a socket.
"""
import socket
import pickle


class micro_client:
    def __init__(self, REQ_DEST):
        self.__STDPORTS = {'LIFE_GEN': 5467, 'CONT_GEN': 5468, 'POP_GEN': 5479, 'PERS_GEN': 5480}

        # address data members
        self.__PORT = self.__STDPORTS[REQ_DEST]
        self.__IP = socket.gethostbyname(socket.gethostname())
        self.__ADDR = (self.__IP, self.__PORT)

        # functional data members        
        self.__HEAD = 64  # header of 64 bytes for message protocol
        self.__DCON = "&END"
        self.__socket = self.define_micro_socket_client() 
    
    def define_micro_socket_client(self):
        """Create and bind socket to port 5467"""
        micro_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        micro_socket_client.connect(self.__ADDR)
        return micro_socket_client
    
    def send_message(self, msg):
        """Sends the message to the server"""
        message = msg.encode('utf-8') 
        message_length = len(message)
        
        send_length = str(message_length).encode('utf-8')
        send_length += b' ' * (self.__HEAD - len(send_length))
      
        self.__socket.send(send_length) # send header with message length
        self.__socket.send(message) # send request message content

    def send_data(self, data):
        """Sends pickled data to the server"""
        data_string = pickle.dumps(data)
        self.__socket.send(data_string)

# main function for test
if __name__ == "__main__":
    client = micro_client('LIFE_GEN') # create a life generator request client
    client.send_message("Generate some life!!")
    client.send_data("Hobbies;Trains")
    client.send_message("&END")



