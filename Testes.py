import unittest
from my_twitter import *

class TestMyTwitter(unittest.TestCase):
    def setUp(self):
        self.my_twitter = MyTwitter()
        self.usuario1 = "@Zacarias"
        self.usuario2 = "@Catarina"
        self.usuario3 = "@Lucas"

    def test_criar_perfil(self):
        self.my_twitter.criar_perfil(self.usuario1)
        perfil = self.my_twitter._MyTwitter__repositorio.buscar(self.usuario1)
        self.assertEqual(perfil.usuario, self.usuario1)

    def test_cancelar_perfil(self):
        self.my_twitter.criar_perfil(self.usuario1)
        self.my_twitter.cancelar_perfil(self.usuario1)
        perfil = self.my_twitter._MyTwitter__repositorio.buscar(self.usuario1)
        self.assertEqual(perfil.is_ativo(), False)

    def test_tweetar(self):
        self.my_twitter.criar_perfil(self.usuario1)
        mensagem = "Meu primeiro tweet!"
        self.my_twitter.tweetar(self.usuario1, mensagem)
        perfil = self.my_twitter._MyTwitter__repositorio.buscar(self.usuario1)
        self.assertEqual(perfil.get_tweets()[-1].mensagem, mensagem)

    def test_seguir(self):
        self.my_twitter.criar_perfil(self.usuario1)
        self.my_twitter.criar_perfil(self.usuario2)
        self.my_twitter.seguir(self.usuario1, self.usuario2)
        perfil_seguidor = self.my_twitter._MyTwitter__repositorio.buscar(self.usuario2)
        self.assertEqual(self.usuario1 in perfil_seguidor.get_seguidores(), True)

if __name__ == "__main__":
    unittest.main()
