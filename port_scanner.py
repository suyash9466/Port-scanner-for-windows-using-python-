import socket
# Input the target IP address
target_ip = (input("Target IP:"))
#Input port range
start_port = int(input("Start Port:"))
end_port = int(input("End Port:"))

def port_scanner(target_ip, start_port, end_port):

    for port in range(start_port, end_port+1):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)

        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        sock.close()
        
port_scanner(target_ip, start_port, end_port)