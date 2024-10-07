import socket

def receive_quote():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 6000))

    quote = client_socket.recv(1024).decode('utf-8')
    print(f"QUOTE OF THE DAY: {quote}")

    client_socket.sendall(b"ACK")
    client_socket.close()

if __name__ == "__main__":
    receive_quote()