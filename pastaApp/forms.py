from django import forms
from .models import Livros

class LivroForm(forms.ModelForm):
    
    livro = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome do livro',
        })
    )

    autor = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome do autor',
        })
    )

    descricao = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Descrição do livro (opcional)',
            'rows': 4,
        })
    )

    class Meta:
        model = Livros
        fields = ['livro', 'autor', 'descricao']