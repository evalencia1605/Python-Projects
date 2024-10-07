import socket
import random
import datetime

quotes = [
    "A penny saved is a penny earned.",
    "Give a man a fish and he eats for a day. Teach a man to fish and he will spend all his money on fishing gear.",
    "Even if the voices are not real, they have some pretty good ideas.",
    "Nothing ventured, nothing gained.",
    "Actions speak louder than words."
]


def log_activity(message):
    with open("server.log", "a") as log_file:
        log_file.write(f"[{datetime.datetime.now()}] {message}\n")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 6000))
    server_socket.listen(1)

    log_activity("Server starting.")
    log_activity("Server listening on port 6000.")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            log_activity(f"[client {client_address}] Connection accepted.")

            quote = random.choice(quotes)
            client_socket.sendall(quote.encode('utf-8'))
            log_activity(f"[client {client_address}] Quote sent.")

            client_socket.recv(1024)
            log_activity(f"[client {client_address}] Client acknowledges quote")

            client_socket.close()
            log_activity(f"[client {client_address}] Connection closed.")

    except KeyboardInterrupt:
        print("Server shutting down.")
        log_activity("Server shutting down.")

    finally:
        server_socket.close()
        log_activity("Server socket closed")


if __name__ == "__main__":
    start_server()


