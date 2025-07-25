import socket


def resolve_domain(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except Exception as e:
        return f"Error resolving domain {target}: {e}"
        