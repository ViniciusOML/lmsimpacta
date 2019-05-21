from django.shortcuts import render, get_object_or_404

from curriculo.models import Curso



def curso(request, sigla):
    c = get_object_or_404(Curso, sigla=sigla)
    context = {
        'curso': c,
        # Aqui substitua o dicionario vazio pelo gerado pelo método
        # monta_matriz
        'matriz': {Curso.monta_matriz}  # c.monta_matriz()
    }
    return render(request, 'curriculo/curso.html', context)
