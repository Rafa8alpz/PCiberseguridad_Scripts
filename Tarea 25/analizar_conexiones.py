#!/usr/bin/python3
import subprocess
import re
from collections import defaultdict

#Ejecucion de bash
result = subprocess.run(['bash','monitor_conexiones.sh'], capture_output=True, text=True)
print(result.stdout)

if result.returncode != 0:
    print("Error de la ejeucion:")
    print(result.stderr)

# Puertos estándar
standard_ports = {22, 25, 80, 465, 587, 8080}

# Diccionario para contar conexiones por IP
ip_count = defaultdict(int)

# Expresión regular para extraer IP y puerto
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+):(\d+)')

# Analizar conexiones
for connection in result.stdout.splitlines():
    match = pattern.search(connection)
    if match:
        ip = match.group(1)
        port = int(match.group(2))
        
        # Contar conexiones por IP
        ip_count[ip] += 1
        
        # Verificar si el puerto es sospechoso
        if port not in standard_ports:
            with open('reporte.txt', 'a') as file:
                file.write(f"Conexion sospechosa detectada: {connection}\n")

# Identificar IPs con múltiples conexiones
for ip, count in ip_count.items():
    if count > 1:
        print(f"IP sospechosa con múltiples conexiones: {ip} ({count} conexiones)")

