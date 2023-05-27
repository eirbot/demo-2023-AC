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
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        print(f"[NEW CONNECTION] {ADDR} connected.")
        file = open("test-uart.bin", "rb")
        data = file.read()
        client.send(data)
        print(f"[{ADDR}] {data}")
        client.close()
        
if __name__ == "__main__":
    main()
    