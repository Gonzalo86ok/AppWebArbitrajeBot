from django.urls import path
from app.views.usuario_view import home_view, registro_usuario

urlpatterns = [
    path('', home_view, name='home'),
    path('registro/', registro_usuario, name='registro_usuario'),
]
