from django.shortcuts import redirect, render
from django.views.decorators import csrf
from numpy import DataSource
from .models import Categoria, Persona
from .forms import PersonaForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def inicio(request):
    return render(request, 'core/inicio.html')
def nose(request):
    return render(request, 'core/nose.html')


def formulario2(request):
    return render(request, 'core/formulario2.html')
def  GaleriaDeFotos(request):
    return render(request, 'core/GaleriaDeFotos.html')

def quienesSomos(request):
    return render(request, 'core/quienesSomos.html')
def mostrar(request):
    persona= Persona.objects.all()
    datos={
        'persona': persona
    }
    return render (request, 'core/mostrar.html', datos)


def forms_persona(request):
    if request.method=='POST':
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid():
            persona_form.save()
            return redirect('home')
    else:
        persona_form= PersonaForm()
    return render(request, 'core/forms_persona.html', {'persona_form': persona_form})


def form_mod_persona(request, id): #recibe de parametro la patente
    persona= Persona.objects.get(nombre=id)
    datos={
        'form': PersonaForm(instance=persona)
    }
    if request.method=='POST':
        formulario=PersonaForm(data=request.POST, instance=persona)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar2')
    return render(request, 'core/form_mod_persona.html', datos)



    