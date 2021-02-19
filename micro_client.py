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
    
    self.__init__():
        self.__HEAD = 64 # header of 64 bytes for message protocol
        self.__PORT = 5467
        self.__IP = socket.gethostbyname(socket.gethostname())
        self.__socket = self.define_micro_socket()
        self.start_listening()

