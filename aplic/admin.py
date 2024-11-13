from django.contrib import admin
from .models import Evento, Administrador, Atividade, Endereco, Responsavel, Residente, Categoria, Inscricao, Feedback, \
    Notificacao


class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1


class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1


class ResponsavelInline(admin.TabularInline):
    model = Responsavel
    extra = 1


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    inlines = [AtividadeInline]
    list_display = ('nome', 'descricao')


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    inlines = [EnderecoInline]
    list_display = ('nome', 'cargo')


@admin.register(Residente)
class ResidenteAdmin(admin.ModelAdmin):
    inlines = [ResponsavelInline]
    list_filter = ('data_nascimento',)


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep')


@admin.register(Responsavel)
class RespostavelAdmin(admin.ModelAdmin):
    inlines = [EnderecoInline]
    list_display = ('telefone', 'celular', 'telefone_comercial')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Inscricao)
class Inscricao(admin.ModelAdmin):
    list_display = ('status', 'dataHora_inscricao')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('comentario', 'nota', 'dataHora')


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('mensagem', 'dataEnvio')
