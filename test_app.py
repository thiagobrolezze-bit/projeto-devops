
import unittest

from app import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_inicio(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 200)

    def test_listar_tarefas(self):
        resposta = self.client.get("/tarefas")
        self.assertEqual(resposta.status_code, 200)

    def test_buscar_tarefa_existente(self):
        resposta = self.client.get("/tarefas/1")
        self.assertEqual(resposta.status_code, 200)

    def test_buscar_tarefa_inexistente(self):
        resposta = self.client.get("/tarefas/999")
        self.assertEqual(resposta.status_code, 404)


if __name__ == "__main__":
    unittest.main()