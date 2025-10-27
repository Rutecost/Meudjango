from django.urls import path
from . import views

urlpatterns = [
    # /produtos
    path('', views.lista_produtos, name='lista_produtos'),

    # /produtos/novo/
    path('novo/', views.novo_produto, name='novo_produto'),

    # /produtos/{id}/
    path('<int:id>/', views.atualizar_produto, name='atualizar_produto'),

    # /produtos/{id}/delete/
    path('<int:id>/delete/', views.deletar_produto, name='deletar_produto'),
]
