import socket

def scan_ports(ip_address, ports=[21, 22, 23, 25, 53, 80, 443, 3306]):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
        except Exception as e:
            continue
    return open_ports