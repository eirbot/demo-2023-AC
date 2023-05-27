import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}")
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[{addr}] {filename}")
        conn.send("Filename received".encode(FORMAT))
        file = open(filename, "wb")
        data = conn.recv(SIZE)
        while data:
            file.write(data)
            data = conn.recv(SIZE)
        file.close()
        conn.close()
        
if __name__ == "__main__":
    main()
    