import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321

#create server socket

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((IP,PORT)) #server will be able to listen at a particular port
    # We are not writing here the listen functon because it is a connectionless protocol
    # Earlier we used to listen the connection requesy
    print(f"Server is up at IP - {IP} : Port - {PORT}")

except socket.error as e:
    print(f"Error in socket creation : {e}")
    sys.exit()


while True:
    try:
        data, addr = s.recvfrom(1024)
        msg, value = data.decode("utf-8").split(",")
        value_c = int(value)
        with open("random.txt","a") as file:
            file.write(f"{value_c}\n")

        print(f"{addr} >> {msg}")

    except Exception as e:
        print(f"Error : {e}")

    except KeyboardInterrupt:
        print("Exit due to Keyboard Interrupt")
        break
    
sys.close()
sys.exit()


