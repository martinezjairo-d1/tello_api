from djitellopy import Tello
import cv2
import time
import os
from .video_uploader import subir_video_a_cdn

def ejecutar_demo_completo():
    carpeta = "C:/dronjdi"
    os.makedirs(carpeta, exist_ok=True)

    # Ruta de guardado fijo para demo
    ruta_video = os.path.join(carpeta, "demo_final.mp4")

    # Preparar dron y cámara
    tello = Tello()
    tello.connect()
    battery = tello.get_battery()
    if battery < 20:
        raise Exception(f"Batería baja ({battery}%)")

    tello.streamon()
    frame_reader = tello.get_frame_read()

    # Comenzar vuelo
    tello.takeoff()
    tello.move_up(20)  # ~1 m total con takeoff

    # Configurar grabación
    ancho, alto = 960, 720
    fps = 30
    duracion_segundos = 5
    total_frames = fps * duracion_segundos

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(ruta_video, fourcc, fps, (ancho, alto))

    # Grabar mientras gira
    try:
        for i in range(total_frames):
            frame = frame_reader.frame
            if frame is not None:
                out.write(frame)
            if i == 0:
                tello.rotate_clockwise(180)
            time.sleep(1 / fps)
    finally:
        out.release()
        tello.streamoff()

    tello.land()
    tello.end()

    # Subir video
    url = subir_video_a_cdn(ruta_video)

    return {
        "battery": battery,
        "ruta": ruta_video,
        "url": url
    }