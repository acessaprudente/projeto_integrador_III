from django.test import TestCase
from model_mommy import mommy
from django.test import Client


class AvaliacaoTestCase(TestCase):

    def setUp(self):
        self.avaliacao = mommy.make('Avaliacao')

    def test_str(self):
        self.assertEquals(str(self.avaliacao), self.avaliacao.user.username)

