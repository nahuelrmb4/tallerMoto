from django.shortcuts import render, redirect
from . forms import motosForm
from .models import M

def motos(request):
    return render(request, 'motos/motos.html')

def crearmotos(request):
    formulario = motosForm()
    contexto={
        'form' : formulario,
        'mensaje': 'Crear motos'
    }
    if request.method =='POST':
        formularioPOST = motosForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('motos')
        else:
            contexto['mensaje']+='-Error en el formulario'
            contexto['form']= formularioPOST
            return render(request, 'motos/formmotos.html', contexto)
    else:
        return render(request, 'motos/formmotos.html', contexto)
    
def listamotos(request):
    motos = M.objects.all()
    context={
        'titulo': 'lista de motos',
        'motos': motos
    }
    return render(request, 'motos/listamotos.html', context)