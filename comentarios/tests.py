from django.test import TestCase
from model_mommy import mommy
from django.test import Client


class ComentarioTestCase(TestCase):

    def setUp(self):
        self.comentario = mommy.make('Comentario')

    def test_str(self):
        self.assertEquals(str(self.comentario), self.comentario.usuario.username)
