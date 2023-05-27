import socket

IP = '192.168.43.200'
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

#receive the file
def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}")
    client, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")
    file = open("test.txt", "wb")
    data = client.recv(SIZE)
    file.write(data)
    print(f"[{addr}] {data}")
    file.close()
    client.close()
    
if __name__ == "__main__":
    main()
    