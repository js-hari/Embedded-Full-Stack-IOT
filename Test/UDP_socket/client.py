import socket
import sys
import random
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321


try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print(f"Client is ready")

except socket.error as e:
    print(f"Error in socket creation : {e}")
    sys.exit()

"""def random_number():
    val = random.randint(1,100)
    
    return val"""




while True:
    try:
        msg = input(">>")
        value = random.randint(1,100)
        data = f"{msg},{value}"
        s.sendto(data.encode("utf-8"),(IP,PORT))
        

    except Exception as e:
        print(f"Error : {e}")

    except KeyboardInterrupt:
        print("Exit due to Keyboard Interrupt")
        break


