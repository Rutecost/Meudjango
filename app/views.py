from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from app.models import Produto


def lista_produtos(request):
    produtos = Produto.objects.order_by('-criado_em')
    context = {'produtos': produtos}
    return render(request, 'lista_produtos.html', context)


@require_http_methods(['GET'])
def formulario_produto(request):
    return render(request, 'formulario.html')


@require_http_methods(['POST'])
def cadastrar_produto(request):
    nome = request.POST.get('nome')
    preco = request.POST.get('preco')

    if nome and preco:
        Produto.objects.create(nome=nome, preco=preco)
        return redirect('lista_produtos')

    contexto = {'erro': 'Preencha nome e preço corretamente.'}
    return render(request, 'novo_produto.html', contexto)


@require_http_methods(['DELETE'])
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()

    contexto = {
        'produto_nome': produto.nome,
        'mensagem': 'Excluído com sucesso.'
    }

    return render(request, template_name='lista_produtos.html')