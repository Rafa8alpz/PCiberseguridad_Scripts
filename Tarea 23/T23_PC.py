#Angel Esau Hernandez Garcia
#Hugo Gael Arredondo Esparza
#Kevin Rafael Ochoa López


import datetime
import pyautogui
import subprocess

try:
    date = datetime.datetime.now()
    name = r"captura_"
    name += str(date.strftime("%Y-%m-%d_%H-%M-%S"))
    name += ".png"
    ss = pyautogui.screenshot()
    ss.save(name)

    print(f"Captura guardada: {name}")
    
except Exception as e:
    print(f"Error al capturar: {e}")

try:
    file_date = datetime.datetime.now()
    file_name = r"proceso_"
    file_name += str(file_date.strftime("%Y-%m-%d_%H-%M-%S"))
    file_name += ".txt"

    salida = subprocess.run(["tasklist"], capture_output=True, text=True, shell=True)

    with open(file_name, "w") as archivo:
        archivo.write(salida.stdout)

    print(f"Procesos guardados en: {file_name}")

except Exception as e:
    print(f"Error en registro: {e}")



    
    
