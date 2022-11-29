
import uuid
from django.db import models
from stdimage.models import StdImageField

       
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-wheelchair ', 'cadeira'),
        ('lni-users', 'Usuários'),
        ('lni-eye', 'olho'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-android', 'Android'),
        ('lni-facebook', 'Facebook'),

    )
    servico = models.CharField('Serviço', max_length=50)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone',max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.servico




class Atividade(Base):
    atividade = models.CharField('Atividade', max_length=20)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.atividade


class Estabelecimento(Base):
    nome = models.CharField('Nome', max_length=100)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        
        
    def __str__(self):
        return self.nome
