#intrgrantes: Angel Esau Hernandez Garcia, Kevin Rafael Ochoa López, Hugo Gael Arredondo Esparza
import subprocess
import pandas as pd
import json

scriptps = "monitor_servicios.ps1"

lineaps = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-file", scriptps], capture_output=True, text=True)

output = lineaps.stdout.strip()
if output:
    servicios = json.loads(output)
    df = pd.DataFrame(servicios)

    df.to_excel('servicios.xlsx', index=False)

    print("Los servicios se guardaron en el archivo: 'servicios.xlsx'.")
else:
    print("No se obtuvo ninguna salida")

