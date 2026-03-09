import requests
import os

def publicar():
    # 1. Configuración (El token lo sacaremos de los Secretos de GitHub)
    token = os.getenv("EAA7XFZC1ikewBQZCWzCaRBhsk4ENJPYIYLoiOBL9dToka1ZCZAVaS0QE5ZAqCCBciVXomHjbzZAjZAKFZBJFWwsZBflFXeXJZCtLVdikZCS3p5NpOyTicYu8Uy8fSczg1ZCsG0hVdriiZA1OJ13eaZASjjzJFWw3DgcJZBNEWALFzCF5ywlB28E7pJplasqgyfmQYaCXYwjqkqUSsavcOLsZA1fWLqvx73VNDnlz43c9PmSCsiAZD")
    page_id = "1012912958570750"
    estacion = "IOZUMB2"
    
    # 2. Mensaje que se publicará (puedes personalizarlo)
    # Nota: Si no tienes API Key, enviamos el link directo para evitar el error de "post vacío"
    mensaje = (
        f"🌤️ Reporte Meteorológico Ozumba ({estacion})\n"
        f"Sigue el clima en tiempo real aquí: "
        f"https://www.wunderground.com/dashboard/pws/IOZUMB2/graph/2026-01-20/2026-01-20/monthly"
        f"📅 Actualizado automáticamente cada hora."
    )

    # 3. Petición POST a Facebook
    url = f"https://graph.facebook.com/v21.0/{1012912958570750}/feed"
    payload = {'message': mensaje, 'access_token': token}
    
    r = requests.post(url, data=payload)
    print(f"Respuesta de Facebook: {r.text}")

if __name__ == "__main__":
    publicar()
