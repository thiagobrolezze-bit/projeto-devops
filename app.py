
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista temporária de tarefas
tarefas = [
    {"id": 1, "titulo": "Aprender GitHub", "concluida": False},
    {"id": 2, "titulo": "Criar um projeto com CI/CD", "concluida": False}
]


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
    "mensagem": "API de tarefas funcionando!",
    "projeto": "Projeto DevOps",
    "versao": "1.0"
})


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefas/<int:tarefa_id>", methods=["GET"])
def buscar_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return jsonify(tarefa)

    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()

    if not dados or "titulo" not in dados:
        return jsonify({"erro": "O campo 'titulo' é obrigatório"}), 400

    novo_id = max([tarefa["id"] for tarefa in tarefas], default=0) + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": dados["titulo"],
        "concluida": False
    }

    tarefas.append(nova_tarefa)

    return jsonify(nova_tarefa), 201


@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def excluir_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa excluída com sucesso"})

    return jsonify({"erro": "Tarefa não encontrada"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)