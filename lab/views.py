from django.shortcuts import render, get_object_or_404
from .forms import PersonaForm
from django.shortcuts import redirect
from .models import Persona

# Create your views here.
def bienvenida(request):
    return render(request, 'lab/bienvenida.html', {})

def agregar(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('agregar')
    else:
        form = PersonaForm()
    return render(request, 'lab/agregar.html', {'form': form})

def consultar(request):
    persona = Persona.objects.all() 
    return render(request, 'lab/consultar.html', {'personas':persona})

def editar(request, pk):
    persona = Persona.objects.get(id=pk)
    form = PersonaForm(instance=persona)

    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
        return redirect('consultar')
    return render(request, 'lab/agregar.html', {'form':form})

def eliminar(request, pk):
    persona = Persona.objects.get(id=pk)
    persona.delete()

    return redirect('/')
