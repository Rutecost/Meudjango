from django.urls import path
from . import views  # importa as views do app clientes

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('<int:id>/', views.lista_clientes, name='cliente'),
]
