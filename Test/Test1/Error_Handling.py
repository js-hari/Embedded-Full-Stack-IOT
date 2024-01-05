import socket
import argparse
import sys

# TRY these lines if got an error then run the EXCEPT and proceed to the execution of FINALLY

def main():
    #parsing means reading the input from te command line
    parser = argparse.ArgumentParser(description= "Soclet Error Example") # an object is created to handle all the inputs
    parser.add_argument('--Host',action="store", dest= "host" , required=False)#It is used the read the value and store it where we find a string names host.
    parser.add_argument('--port' ,action="store" , dest="port" , type=int,required=False)#whatever we type on the keyboard comes in the string format.
    parser.add_argument('--file' ,action="store" , dest="file")

    parser.add_argument
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    file = given_args.file







#connection errors are known as gaierrors

#after getting we need to read a file using the get method 