from django.urls import path
from .views import Home, UpdateUsuario, DeleteUsuario

app_name = "nose"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('actualizar/<int:pk>/', UpdateUsuario.as_view(), name='actualizar'),
    path('eliminar/<int:pk>/', DeleteUsuario.as_view(), name='eliminar'),

]