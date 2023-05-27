import socket
import shutil
import os
import glob

IP = '192.168.43.200'
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def copy_file_to_usb(usb_path, file_pattern, destination_path):
    # Detect the USB port where the file is located
    usb_files = glob.glob(usb_path + file_pattern)

    # Display a list of files found on the USB and allow the user to select one
    print("USB files:")

    selected_file = usb_files[0]

    # Copy the file to the destination
    shutil.copy(selected_file, destination_path)
    print("File copied successfully!")

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
    server.close()
    
if __name__ == "__main__":
    usb_path = '/media/eirbot/NODE_F446RE3/'  # Specify the USB path
    file_pattern = 'test.bin'  # Specify the file pattern or extension
    destination_path = '/home/demo-2023-AC/eirbot-remote-televerser/'  # Specify the destination directory
    
    main()
    copy_file_to_usb(destination_path, file_pattern, usb_path)