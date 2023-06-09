import socket

IP = '192.168.43.200'
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[NEW CONNECTION] {ADDR} connected.")
    file = open("test-uart.bin", "rb")
    data = file.read()
    while data:
        client.send(data)
        data = file.read(SIZE)
        
    print(f"[{ADDR}] {data}")
    client.close()
        
if __name__ == "__main__":
    main()
    