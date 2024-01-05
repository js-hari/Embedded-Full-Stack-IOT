"""When we deal with low level network functions some times
-> The usual string notation of ipaddresses are not very useful 
-> They need to be converted to the packed 32-bit binary formats
-> following teo utilities ofpython library are to be used
-> inet_aton() and inet_atoa()
-> """

import socket




# 1->>>>>>>>>>>>>>>>>>>>     CONVERSION F IPV4 ADRRESSES TO HEXADECIAL NOTATION     <<<<<<<<<<<<<<<<<<<<<<<<<<


from binascii import hexlify
#hexlify will convert the ascii code into the hexadecimal notation

def convert_ipv4_addr():
    for ip in ['127.0.0.1','192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip)
        

        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print(""" The given IP address is : {}
                    Packed IP address is :  {} 
                    Unpacked IP address is : {}""".format(ip,packed_ip_addr,unpacked_ip_addr))



if __name__ == "__main__":
    convert_ipv4_addr()





# 2->>>>>>>>>>>>>>>>>>>>>>>>>>>   GET THE PORT NAME AND THEIR SERVICE NAME   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



def find_service_name():
    protocol_name = 'tcp' #try with udp as well
    for port in [80,25,443,993,110,111,43]:
        print(" PORt: {} | Service Name : {}".format(port,socket.getservbyport(port,protocol_name)))

    print("PORT : {} | Service Name : {}".format(53,socket.getservbyport(53,'udp')))
    
if __name__ == "__main__":
    find_service_name()



# 3->>>>>>>>>>>>>>>>>>>>>>>>>>  DATA CONVERSION TO THE NETWORK BYTE ORDER  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def convert_integer():
    data = 1234
    #conversion to 32 bit
    print(f"""
            Original : {data}
            long host byte order : {socket.ntohl(data)} 
            network byte order : {socket.htonl(data)}""")#long and short host reperesentations are different
    print(f"""
            Original : {data}
            short host byte order : {socket.ntohs(data)}
            network byte order : {socket.htons(data)}""")
    

if __name__ == "__main__":
    convert_integer()
    print("")





# 4->>>>>>>>>>>>>>>>  GETTING DEFAULT SOCKET TIMEOUT AND SETTING THE SOCKET TIMEOUT  <<<<<<<<<<<<<<<<<<<<<<<<


# we must have a timeout parameter for the socket and if takes much time than that we should get some result.
def test_socket_timeut():
    #create socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    print(f"Default Socket Timeout : {s.gettimeout()}")

    #set socket timeout 

    s.settimeout(50)
    print(f"Current SOcket Timeout : {s.gettimeout()}")

if __name__ == "__main__":
    test_socket_timeut()
    

