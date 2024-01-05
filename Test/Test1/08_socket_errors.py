# python script
# 08_socket_errors.py
# Himanshu Tripathi
# In any networking application, it is very common that one end is trying to connect,
# but the other party is not responding due to networking media failure
# or any other reason.
# The Python socket library has an elegant method of handing these errors via the socket.error
# exceptions.
# to test the code follow these commands in terminal
# python 08_socket_errors.py --host=www.pytgo.org --port=8080 --file=08_socket_errors.py
# The above command produces error <Address related error>
# python 08_socket_errors.py --host=www.python.org --port=8080 --file=08_socket_errors.py
# The above command produces error <Connection error>
# python 08_socket_errors.py --host=www.python.org --port=80 --file=08_socket_errors.py
# The above command produces result

import socket
import argparse
import sys


def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description="socket error example")
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store",
                        dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # first try-except block - create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error in socket creation: {e}")
        sys.exit(1)

    # second try-except block - connect with given host/ port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f"Address related error connecting to server: {e}")
        sys.exit(1)
    except socket.error as e:
        print(f"connection error: {e}")
        sys.exit(1)

    # third try-except block - sending data
    try:
        s.sendall(f"GET {filename} HTTP/1.0\r\n\r\n".encode("utf-8"))
    except socket.error as e:
        print(f"Error sending data: {e}")
        sys.exit(1)

    while True:
        # Fourth try-except block - waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print(f"Error receiving data: {e}")
            sys.exit(1)
        if not len(buf):
            break
        # write the received data
        sys.stdout.write(buf.decode('utf-8'))


if __name__ == "__main__":
    main()

