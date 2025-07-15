from djitellopy import Tello
import time
import cv2
import os
import time

def ejecutar_demo_vuelo():
    tello = Tello()
    tello.connect()

    battery = tello.get_battery()
    if battery < 20:
        raise Exception(f"Batería baja ({battery}%)")

    tello.takeoff()
    tello.move_up(50)  # Sube a 1.5 m aprox

    tello.rotate_clockwise(180)  # Gira 180 grados

    time.sleep(5)  # Se queda en el aire un momento tras girar (total: 3+5 = 8s)

    tello.land()
    tello.end()

    return {"battery": battery}

def grabar_video():
    carpeta = "C:/dronjdi"
    os.makedirs(carpeta, exist_ok=True)  # Crea la carpeta si no existe

    # Buscar el próximo número disponible
    i = 1
    while os.path.exists(os.path.join(carpeta, f"dron{i}.mp4")):
        i += 1
    nombre_archivo = f"dron{i}.mp4"
    ruta_video = os.path.join(carpeta, nombre_archivo)

    # Configurar dron y grabación
    tello = Tello()
    tello.connect()
    tello.streamon()
    frame_reader = tello.get_frame_read()

    ancho, alto = 960, 720
    fps = 30
    duracion_segundos = 5
    total_frames = fps * duracion_segundos

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(ruta_video, fourcc, fps, (ancho, alto))

    try:
        for _ in range(total_frames):
            frame = frame_reader.frame
            if frame is not None:
                out.write(frame)
            time.sleep(1 / fps)
    finally:
        out.release()
        tello.streamoff()
        tello.end()

    return {"ruta": ruta_video}