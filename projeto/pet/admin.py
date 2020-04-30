from django.contrib import admin
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'bairro', 'tipo']


admin.site.register(Pet, PetAdmin)
