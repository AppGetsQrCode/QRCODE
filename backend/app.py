from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return jsonify({
        "status": "ok",
        "mensagem": "Servidor Python funcionando!"
    })


@app.route("/teste")
def teste():
    return jsonify({
        "selenium": "preparado para a próxima etapa"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
