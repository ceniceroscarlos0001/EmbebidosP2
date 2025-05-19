#!/usr/bin/env python3
import serial
import socket

# Configuración del puerto serial (Arduino)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

# Configuración del socket TCP
HOST = "192.168.2.3"  # Dirección IP de la PC Ubuntu
PORT = 5000           # Puerto TCP

try:
    # Crear socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print(f"[INFO] Conectado al servidor TCP {HOST}:{PORT}")
except Exception as e:
    print(f"[ERROR] No se pudo conectar al servidor: {e}")
    exit(1)

# Bucle de lectura y envío
try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if ',' in line:
                binario, timestamp = line.split(',')
                mensaje = f"{binario},{timestamp}\n"
                print(f"Enviando: {mensaje.strip()}")
                sock.sendall(mensaje.encode('utf-8'))
except KeyboardInterrupt:
    print("\n[INFO] Interrupción por teclado. Cerrando conexión.")
finally:
    sock.close()
    ser.close()
