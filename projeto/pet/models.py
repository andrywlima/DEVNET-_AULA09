from django.db import models


class Pet(models.Model):

    bairro = models.CharField(max_length=100)
    descricao = models.TextField()
    celular = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True, blank=True)
   # data_perdido = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='pet', blank=True, null=True)
    os_choice = (
        ('Gato', 'Gato'),
        ('Cachorro', 'Cachorro'),
        ('Outro', 'Outro'),
    )
    tipo  = models.CharField(max_length=30, blank=True, null=True, choices=os_choice)