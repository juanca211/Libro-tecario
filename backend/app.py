
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def inicio():
    return jsonify({
        "mensaje": "Backend de Libro-tecario funcionando correctamente"
    })


@app.get("/api/health")
def health():
    return jsonify({
        "estado": "ok"
    })


if __name__ == "__main__":
    app.run(debug=True)
