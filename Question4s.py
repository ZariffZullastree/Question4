import socket
import threading
import random

quotes = [
        "Siapa cili dia pedas, kalau miskin dia malas",
        "No Pain No Gain, Just Do It - Nike",
        "My boy, one small breeze doesn't make a wind storm - John McGraw",
        "The most wasted day of all is that on which we have not laughed. - >

]

def handle_client(client_socket):
    quote = random.choice(quotes)
    client_socket.send(quote.encode())
    client_socket.close()

def main():
    host = "192.168.121.136"
    port = 8484

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host,port))

    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            client_handler = threading.Thread(target=handle_client, args=(cl>
            client_handler.start()

    except KeyboardInterrupt:
        print(f"Bye Bye.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

