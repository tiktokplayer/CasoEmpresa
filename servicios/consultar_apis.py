import requests

def consultar_api(rut):
    URL = f"https://api.boostr.cl/rut/name/{rut}.json"
    response = requests.get(URL)
    
    if response.status_code == 200:
        print("Consulta exitosa")
        print('Data: ', response.json())
    else:
        print("Error al consultar la API:", response.text)


