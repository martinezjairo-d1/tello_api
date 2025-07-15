import requests

def subir_video_a_cdn(ruta_video: str) -> str:
    
    url = "https://kuntur-cdn.onrender.com/upload-backblaze/"
    archivos = {"video": open(ruta_video, "rb")}

    try:
        respuesta = requests.post(url, files=archivos)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos.get("url")
    except Exception as e:
        raise Exception(f"Error al subir el video al CDN: {str(e)}")
