from django.contrib import admin

from .models import Atividade, Servico, Estabelecimento


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('atividade', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'atividade', 'ativo', 'modificado')

