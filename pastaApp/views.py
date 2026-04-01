from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Livros
from .forms import LivroForm


@login_required
def lista_livros(request):
    livros = Livros.objects.filter(usuario=request.user).order_by('-criada_em')
    return render(request, 'pastaApp/lista_livros.html', {'livros': livros})


@login_required
def detalhe_livro(request, slug):
    livro = get_object_or_404(Livros, slug=slug, usuario=request.user)
    return render(request, 'pastaApp/detalhe_livro.html', {'livro': livro})


@login_required
def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user
            livro.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'pastaApp/form.html', {'form': form, 'acao': 'Adicionar'})


@login_required
def editar_livro(request, slug):
    livro = get_object_or_404(Livros, slug=slug, usuario=request.user)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'pastaApp/form.html', {'form': form, 'acao': 'Editar'})


@login_required
def deletar_livro(request, slug):
    livro = get_object_or_404(Livros, slug=slug, usuario=request.user)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'pastaApp/confirmar_delete.html', {'livro': livro})



class Registro(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

