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


class micro_client:
    def __init__(self):
        #self.__init__():
        self.__HEAD = 64  # header of 64 bytes for message protocol
        self.__PORT = 5467
        self.__IP = socket.gethostbyname(socket.gethostname())
        self.__ADDR = (self.__IP, self.__PORT)
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


# main function for test
if __name__ == "__main__":
    client = micro_client()
    client.send_message("life generator")
    client.send_message('&END')



