#!/usr/bin/env python3


def socket_listener(HOST,  PORT, timeout_length):
    import socket
    import time
    initial_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        data_storage = bytes()
        with conn:
            while True:
                data = conn.recv(1024)
                print(data)
                data_storage = data_storage + data
                if time.time() - initial_time == timeout_length:
                    break
                if not data:
                    break
    return data_storage

def bytes_to_file(bytes_input):
    result = bytes_input.decode(encoding="utf-8", errors="ignore")
    log = open('log.txt', "r+")
    log.writelines(result)
    log.close()
    return result



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 21        # Port to listen on (non-privileged ports are > 1023)
SECONDS = 180 # Time in seconds you want the port to listen on

bytes_to_file(socket_listener(HOST, PORT, SECONDS))
