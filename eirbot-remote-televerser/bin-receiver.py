import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = ('192.168.43.200', PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = server.sockopt(socket.SOL_SOCKET, 25, 'wlan0')
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on 192.168.43.200")
    
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")
    filename = conn.recv(SIZE).decode(FORMAT)
    file = open(filename, "wb")
    conn.send("Filename received".encode(FORMAT))
    data = conn.recv(SIZE).decode(FORMAT)
    file.write(data)
    file.close()
    print(f"[{addr}] {data}")
    conn.close()
    
if __name__ == "__main__":
    main()