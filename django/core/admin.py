from django.contrib import admin
from .models import Objeto, Pessoa

class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'caracteristica', 'dataperdido')

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Objeto, ObjetoAdmin)

