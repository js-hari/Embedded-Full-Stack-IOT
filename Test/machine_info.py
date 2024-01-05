import socket



def get_remote_machine_info():
    try:
        host_name = "www.google.com"
        ip_addr = socket.gethostbyname(host_name)
        print(f"IP address of {host_name} is {ip_addr}")
    except Exception as e:
        print(f"Error : {e}")



#if __name__ == "__main__":
get_remote_machine_info()







