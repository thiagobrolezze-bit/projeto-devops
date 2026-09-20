
import unittest
import app as app_module
from app import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

        # Reinicia a lista de tarefas antes de cada teste
        app_module.tarefas.clear()
        app_module.tarefas.extend([
            {"id": 1, "titulo": "Aprender GitHub", "concluida": False},
            {"id": 2, "titulo": "Criar um projeto com CI/CD", "concluida": False}
        ])

    # TESTE 1
    def test_inicio(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 200)

        dados = resposta.get_json()
        self.assertEqual(
    dados["mensagem"],
    "API de tarefas funcionando com sucesso!"
)

    # TESTE 2
    def test_listar_tarefas(self):
        resposta = self.client.get("/tarefas")
        self.assertEqual(resposta.status_code, 200)

        dados = resposta.get_json()
        self.assertEqual(len(dados), 2)

    # TESTE 3
    def test_buscar_tarefa_existente(self):
        resposta = self.client.get("/tarefas/1")
        self.assertEqual(resposta.status_code, 200)

        dados = resposta.get_json()
        self.assertEqual(dados["id"], 1)
        self.assertEqual(dados["titulo"], "Aprender GitHub")

    # TESTE 4
    def test_buscar_tarefa_inexistente(self):
        resposta = self.client.get("/tarefas/999")
        self.assertEqual(resposta.status_code, 404)

    # TESTE 5
    def test_criar_tarefa(self):
        resposta = self.client.post(
            "/tarefas",
            json={"titulo": "Estudar Docker"}
        )

        self.assertEqual(resposta.status_code, 201)

        dados = resposta.get_json()
        self.assertEqual(dados["titulo"], "Estudar Docker")
        self.assertFalse(dados["concluida"])

    # TESTE 6
    def test_criar_tarefa_sem_titulo(self):
        resposta = self.client.post(
            "/tarefas",
            json={}
        )

        self.assertEqual(resposta.status_code, 400)

    # TESTE 7
    def test_excluir_tarefa(self):
        resposta = self.client.delete("/tarefas/1")
        self.assertEqual(resposta.status_code, 200)

        resposta_busca = self.client.get("/tarefas/1")
        self.assertEqual(resposta_busca.status_code, 404)


if __name__ == "__main__":
    unittest.main()
