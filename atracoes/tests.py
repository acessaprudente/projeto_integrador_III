from django.test import TestCase
from model_mommy import mommy
from django.test import Client


class AtracaoTestCase(TestCase):

    def setUp(self):
        self.atracao = mommy.make('Atracao')

    def test_str(self):
        self.assertEquals(str(self.atracao), self.atracao.nome)

