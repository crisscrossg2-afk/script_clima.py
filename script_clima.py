import requests
import os

def publicar():
    # GitHub lee el secreto que guardaste en Settings
    token = os.getenv("EAA7XFZC1ikewBQys1skMSD6UsdZBdcOabwcqQ6uMrCjEJQ72T7okNwwlAIZC7B1kEZARt7T5ZBhPtKlhZBdhGQj7TwEPZAFlbuloaB9xENaHDOQbqf4ZBsgTXZApwEjZBuO3QvPOP3IcuT0HiNrVLZBKXFxQzahBdkv0TAA5UkO5PxP3rHRApDUIG4bYQhusygMku3qXf39IRNDUhBKaCZBBU0wgwrYYZALOgfQxZCrRDHkpObEo9B") 
    
    # Tu ID de página (sin comillas extras en la URL abajo)
    page_id = "1012912958570750"
    
    mensaje = (
        "📊 Reporte Meteorológico Ozumba\n"
        "Estación: IOZUMB2\n"
        "Consulta en vivo: https://www.wunderground.com/dashboard/pws/IOZUMB2\n"
        "🕒 Actualización horaria automática."
    )

    # REVISA ESTA LÍNEA: No debe tener comillas dentro de las llaves ni al final de feed
    url = f"https://graph.facebook.com/v21.0/1012912958570750/feed"
    
    payload = {
        'message': mensaje,
        'access_token': token
    }
    
    # Realizar la publicación
    response = requests.post(url, data=payload)
    
    # Esto te confirmará el éxito en la pestaña Actions
    print(f"Respuesta de Facebook: {response.text}")

if __name__ == "__main__":
    publicar()
