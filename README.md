
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
