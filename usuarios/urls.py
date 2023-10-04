from django.urls import path
from . import views # O ponto faz com que a importação seja dentro desta pasta

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
]
