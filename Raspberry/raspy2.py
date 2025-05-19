#!/usr/bin/env python3
import serial
import socket
from datetime import datetime

# ============ CONFIGURACIÓN ============

# Puerto serial del Arduino
SERIAL_PORT = '/dev/ttyACM0'
BAUDRATE = 9600

# IP y puerto de la PC host con Windows
HOST_IP = '192.168.1.100'  # <-- Cambia esto por la IP de tu PC con Windows
HOST_PORT = 65432

# Archivo para guardar datos localmente
LOG_FILE = "lecturas_arduino.txt"

# ============ INICIALIZACIÓN SERIAL ============
ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
ser.reset_input_buffer()

# ============ CONEXIÓN TCP/IP ============
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Conectando a {HOST_IP}:{HOST_PORT}...")

try:
    client_socket.connect((HOST_IP, HOST_PORT))
    print("✅ Conexión establecida con la PC host.")
except Exception as e:
    print(f"❌ No se pudo conectar con la PC host: {e}")
    exit(1)

# ============ BUCLE PRINCIPAL ============
try:
    with open(LOG_FILE, "a") as log_file:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()

                if line:
                    # Agrega marca de tiempo legible al archivo
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log_entry = f"{timestamp} - {line}"
                    print(log_entry)

                    # Guardar en archivo
                    log_file.write(log_entry + "\n")
                    log_file.flush()

                    # Enviar por TCP
                    try:
                        client_socket.sendall((line + "\n").encode())
                    except Exception as e:
                        print(f"⚠️ Error al enviar por TCP: {e}")
except KeyboardInterrupt:
    print("\n🛑 Interrumpido por el usuario.")
finally:
    client_socket.close()
    ser.close()
