í#Angel Esau Hernandez Garcia
#Hugo Gael Arredondo Esparza
#Kevin Rafael Ochoa López


# Usar la API de Have I been pwn?
import requests
import json
import logging
import getpass
import argparse
import six

if not six.PY3:
    raise Exception("Se requiere Python 3 para ejecutarse")

# Preguntar correo a revisar
parser = argparse.ArgumentParser(description="Email del usuario")
parser.add_argument("-email1", dest="email", required=True, help="El email a verificar")
args = parser.parse_args()  # Analizar los argumentos
email = args.email  # Obtener el email

# Pedir la API key
apikey = getpass.getpass(prompt="Ingresa el apikey:")
headers = {
    'Content-Type': 'application/json',
    'api-version': '3',
    'User-Agent': 'python',
    'hibp-api-key': apikey
}
# Solicitud
url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'
try: 
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        encontrados = len(data)
        
        if encontrados > 0:
            print("Los sitios en los que se ha filtrado el correo", email, "son:")
            for filtracion in data:
                nombre = filtracion.get("Name", "Desconocido")
                fecha_filtracion = filtracion.get("Date", "Desconocida")
                dominio = filtracion.get("Domain", "No disponible")
                
                # Crear reporte
                reporte = f"""
                Nombre del correo: {email}
                Nombre de la filtración: {nombre}
                Fecha de la filtración: {fecha_filtracion}
                Dominio afectado: {dominio}
                """
                try:
                    with open('reporte_filracionemail.txt', 'a') as file:
                        file.write(reporte)
                except IOError as e:
                    logging.error(f"Error al escribir en el archivo: {e}")
                    
        else:
            print("El correo", email, "no ha sido filtrado")
        
        for filtracion in data:
            print(filtracion["Name"])
        
        msg = f"{email} Filtraciones encontradas: {str(encontrados)}"
        print(msg)
        
        logging.basicConfig(filename='hibpINFO.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p",
                            level=logging.INFO)
        logging.info(msg)
    else:
        msg = r.text
        print(msg)
        
        logging.basicConfig(filename='hibpERROR.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %H:%M:%S",
                            level=logging.ERROR)
        logging.error(msg)

except requests.exceptions.RequestException as errorconexion:
    logging.error(f"Error de conexión: {errorconexion}")
