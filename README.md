
# 🛰️ Tello API - Backend de Vuelo y Grabación

Este proyecto es una API REST desarrollada en Python con Flask que permite:

- Controlar un dron DJI Tello (despegue, giro, aterrizaje).
- Grabar videos del dron en vuelo.
- Subir esos videos a un CDN mediante una API externa.

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Git
- Acceso físico a un dron DJI Tello
- Conexión directa por Wi-Fi al dron desde el PC

---

## 🚀 Instrucciones de instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/martinezjairo-d1/tello_api.git
cd tello_api
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

- En **Windows**:
```bash
venv\Scripts\activate
```

- En **Mac/Linux**:
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 📁 Crear carpeta de grabaciones

Antes de ejecutar el sistema, asegúrate de crear la carpeta donde se guardarán los videos:

```bash
mkdir C:\dronjdi
```

---

## ▶️ Ejecutar el servidor

```bash
python run.py
```

El servidor se levantará en:

```
http://localhost:5000
```

---

## 🌐 Exponer el backend con Ngrok

Para que el backend Flask sea accesible desde otras redes (por ejemplo, desde una app móvil desarrollada con Expo Go), se puede usar [ngrok](https://ngrok.com/), una herramienta que crea túneles seguros desde internet hacia tu entorno local.

### 🔧 1. Instalar ngrok

#### Opción A: usando npm
```bash
npm install -g ngrok
```

#### Opción B: descargando desde la web
1. Ir a https://ngrok.com/download
2. Descargar e instalar según tu sistema operativo
3. Verificar instalación:
```bash
ngrok version
```

### 🔐 2. Conectar tu cuenta de ngrok

1. Crear una cuenta gratuita en https://ngrok.com
2. Obtener tu authtoken desde: https://dashboard.ngrok.com/get-started/setup
3. Configurar el token en tu sistema:
```bash
ngrok config add-authtoken TU_AUTHTOKEN
```

### 🚀 3. Ejecutar el backend Flask

Asegúrate de que el backend esté corriendo localmente:

```bash
python run.py
```

### 🌍 4. Crear túnel público con ngrok

En otra terminal, ejecuta:

```bash
ngrok http 5000
```

Esto creará una URL pública como:

```
https://xxxxxx.ngrok-free.app
```

Esa es la URL que deben usar las aplicaciones externas para consumir los endpoints de este backend.

### 🔒 5. (Opcional) Seguridad por token

Puedes proteger la API pública añadiendo una verificación simple en Flask:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
API_TOKEN = "123456"

@app.before_request
def verificar_token():
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
```

Y en el frontend deben incluir el token en los headers:

```js
fetch("https://xxxxxx.ngrok-free.app/api/vuelo", {
  method: "POST",
  headers: {
    Authorization: "Bearer 123456"
  }
});
```

---

## 📡 Endpoints disponibles

### 📍 `POST /api/vuelo`

Controla el vuelo del dron:

- Despega
- Sube a 1.5 m
- Gira 180°
- Espera unos segundos
- Aterriza

**Respuesta JSON:**

```json
{
  "success": true,
  "battery": 85
}
```

---

### 📍 `POST /api/grabar`

Graba un video de 5 segundos mientras el dron está en el aire y lo guarda en:

```
C:\dronjdi\dron1.mp4, dron2.mp4, ...
```

**Respuesta JSON:**

```json
{
  "success": true,
  "ruta": "C:/dronjdi/dron3.mp4"
}
```

---

### 📍 `POST /api/video`

Envía el video más reciente (ej. `backtest.mp4`) a una API externa que lo sube a un CDN (BunnyCDN o Backblaze).

**Respuesta JSON:**

```json
{
  "success": true,
  "url": "https://cdn-backblaze.ejemplo.com/dron4.mp4"
}
```

> Asegúrate de que la API externa esté activa y accesible.

---

## ✍️ Autor

Jairo Martínez – julio 2025
