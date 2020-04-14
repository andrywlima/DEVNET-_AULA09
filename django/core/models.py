from django.db import models


class Objeto(models.Model):
    nome = models.CharField('Nome', max_length=20)
    caracteristica = models.CharField('Caracteristica', max_length=200)
    dataperdido = models.DateTimeField('Data perdido')

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return self.nome