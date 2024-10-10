import socket #Import socket module for server client modification
import random #Import random so it selects a random quote
import datetime #Import datetime to log timestamps for server activity

quotes = [
    "A penny saved is a penny earned.",
    "Give a man a fish and he eats for a day. Teach a man to fish and he will spend all his money on fishing gear.",
    "Even if the voices are not real, they have some pretty good ideas.",
    "Nothing ventured, nothing gained.",
    "Actions speak louder than words."
]

#Function to log server activity to a file
def log_activity(message): 
    with open("server.log", "a") as log_file:
        log_file.write(f"[{datetime.datetime.now()}] {message}\n")

#Function to start server
def start_server():

    #Creating a new socket with IPv4 and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Binding the socket to "localhost" on port 6000
    server_socket.bind(('localhost', 6000))
    
    #Listen for 1 client at a time
    server_socket.listen(1)

    log_activity("Server starting.")
    log_activity("Server listening on port 6000.")

    try:
        #Server loop to handle multiple client connections
        while True:
            #Accept a new client connection
            client_socket, client_address = server_socket.accept()
            log_activity(f"[client {client_address}] Connection accepted.")

            #Randomly select a quote and send it to the client
            quote = random.choice(quotes)
            client_socket.sendall(quote.encode('utf-8'))
            log_activity(f"[client {client_address}] Quote sent.")

            #Receive acknowledgment from the client
            client_socket.recv(1024)
            log_activity(f"[client {client_address}] Client acknowledges quote")

            #Close the client connection
            client_socket.close()
            log_activity(f"[client {client_address}] Connection closed.")

    except KeyboardInterrupt:
        # Handle server shutdown on Ctrl+C
        print("Server shutting down.")
        log_activity("Server shutting down.")

    finally:
        #Ensure the socket is properly closed during shutdown
        server_socket.close()
        log_activity("Server socket closed")


if __name__ == "__main__":
    start_server()


