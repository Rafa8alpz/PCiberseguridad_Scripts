import requests
import json
import logging
import getpass


logging.basicConfig(filename='hibpINFO.log',
                    format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p",
                    level=logging.INFO)

logging.basicConfig(filename='hibpERROR.log',
                    format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S",
                    level=logging.ERROR)


key = getpass.getpass(prompt="Ingresa la API Key:")


headers = {
    'content-type': 'application/json',
    'api-version': '3',
    'User-Agent': 'python',
    'hibp-api-key': key
}


email = input("Ingrese el correo a investigar: ")


url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()      
    
    data = response.json()
    encontrados = len(data)
    
    if encontrados > 0:
        print(f"Los sitios en los que se ha filtrado el correo {email} son:")
        msg = f"{email} Filtraciones encontradas: {encontrados}"
    else:
        print(f"El correo {email} no ha sido filtrado")
        msg = f"{email} No se encontraron filtraciones."

    
    with open('breaches.txt', 'w') as file:
        for filtracion in data:
            name = filtracion.get("Name", "N/A")
            domain = filtracion.get("Domain", "N/A")
            date = filtracion.get("BreachDate", "N/A")
            description = filtracion.get("Description", "N/A")
            file.write(f"Nombre: {name}\nDominio: {domain}\nFecha: {date}\nDescripción: {description}\n\n")
            print(f"Nombre: {name}\nDominio: {domain}\nFecha: {date}\nDescripción: {description}\n")

    logging.info(msg)

except requests.RequestException as e:
    error_msg = f"Error al realizar la solicitud: {e}"
    logging.error(error_msg)
    print(error_msg)

except Exception as e:
    unexpected_error_msg = f"Error inesperado: {e}"
    logging.error(unexpected_error_msg)
    print("Se produjo un error inesperado. Revisa el archivo de log para más detalles.")

finally:
    print("Proceso completado.")
