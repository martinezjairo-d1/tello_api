from flask import Blueprint, jsonify
from .drone_controller import ejecutar_demo_vuelo
from .video_uploader import subir_video_a_cdn
from .drone_controller import grabar_video
from .demo_controller import ejecutar_demo_completo

api = Blueprint('api', __name__)

@api.route('/api/vuelo', methods=['POST'])
def demo_flight():
    try:
        resultado = ejecutar_demo_vuelo()
        return jsonify({"success": True, **resultado})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@api.route('/api/video', methods=['POST'])
def subir_video():
    try:
        ruta_video = "C:/dronjdi/backtest.mp4"
        url = subir_video_a_cdn(ruta_video)
        return jsonify({"success": True, "url": url})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@api.route('/api/grabar', methods=['POST'])
def grabar():
    try:
        resultado = grabar_video()
        return jsonify({"success": True, **resultado})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@api.route('/api/demo', methods=['POST'])
def demo_completo():
    try:
        resultado = ejecutar_demo_completo()
        return jsonify({"success": True, **resultado})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500