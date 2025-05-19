#!/usr/bin/env python3
import socket

HOST = "0.0.0.0"  # Escucha en todas las interfaces
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[INFO] Servidor escuchando en {HOST}:{PORT}")
    
    conn, addr = s.accept()
    with conn:
        print(f"[INFO] Conexión establecida desde {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[RECEIVED] {data.decode('utf-8').strip()}")
