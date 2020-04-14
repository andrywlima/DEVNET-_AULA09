from django.urls import path
from .views import index, contato, objeto


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('objeto/<int:pk>', objeto, name='objeto')
]



