import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path
from django.test import Client
from django.urls import reverse_lazy
from core.forms import ContatoForm


#TEST MODELS

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class AtividadeTestCase(TestCase):

    def setUp(self):
        self.atividade = mommy.make('Atividade')

    def test_str(self):
        self.assertEquals(str(self.atividade), self.atividade.atividade)


class EstabelecimentoTestCase(TestCase):

    def setUp(self):
        self.estabelecimento = mommy.make('Estabelecimento')

    def test_str(self):
        self.assertEquals(str(self.estabelecimento), self.estabelecimento.nome)
        

 # TEST VIEWS
  
  
class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Felicity Jones',
            'assunto': 'Meu assunto'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
        

# TESTE CONTFORM


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'felicity@gmail.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Uma mensagem qualquer'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)  # ContatoForm(request.POST)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)
