import socket


def main():
    host = "192.168.121.136"
    port = 8484

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host,port))

    quote = client_socket.recv(1024).decode()
    print(f"Quote of the Day <3: {quote}")

    client_socket.close()

if __name__ == "__main__":
    main()
