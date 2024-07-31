
import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Para obtener la temperatura en grados Celsius
    }
    response = requests.get(base_url, params=params)
    # response.url (Imprime la URL de la solicitud)
    # response.status_code (Imprime el código de estado de la respuesta)
    # response.json() (Imprime el contenido de la respuesta)
    if response.status_code == 200:
        return response.json()
    else:
        return None