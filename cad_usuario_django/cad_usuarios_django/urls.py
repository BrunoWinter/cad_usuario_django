
from app_cad_usuario import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
