import socket

def receive_quote():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to the server running on 'localhost' at port 6000
    client_socket.connect(('localhost', 6000))

    #Receive the quote from the server (maximum buffer size of 1024 bytes)
    quote = client_socket.recv(1024).decode('utf-8')
    
    #Printing the quote to the client
    print(f"QUOTE OF THE DAY: {quote}")

    # Send acknowledgment to the server that the quote was received
    client_socket.sendall(b"ACK")
    
    #Close the socket connection
    client_socket.close()

if __name__ == "__main__":
    receive_quote()