from django.shortcuts import render
from .models import *
from .forms import ContactoForm
from django.contrib import messages
# Create your views here.
def index(request):
    servicios = Servicio.objects.all()
    
    aux = {
        'lista' : servicios,
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            aux["mensaje"] = "Contacto enviado"
        else:
            aux["form"] = formulario
    return render(request, 'core/index.html', aux)

def about(request):
    return render(request, 'core/about.html')

def account_locked(request):
    return render(request, 'core/account_locked.html')

def contact(request):
    data = {
        'form' : ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #data["mensaje"] = "Contacto enviado"
            messages.success(request, "Contacto enviado. Nos pondremos en contacto contigo.")
        else:
            data['form'] = formulario
            messages.error(request, "No se pudo enviar el contacto. Por favor, intenta de nuevo.")
            
    return render(request, 'core/contact.html', data)

def service(request):
    return render(request, 'core/service.html')

def listar_servicios(request):
    servicios = Servicio.objects.all()
    
    aux = {
        'lista' : servicios
    }
    return render(request, 'core/service.html', aux) 

def error(request, exception=None):
    return render(request, 'error.html')