from django.shortcuts import render_to_response, get_object_or_404
from principal.models import *
from django.template.context import RequestContext
from forms import *
from principal.models import Usuario
from django.http import HttpResponseRedirect, HttpResponse
def index(request):
    return render_to_response('index.html')# Create your views here.
def login(request):
    if request.method=="POST":
        print request
        usuario = Usuario.objects.filter(username="")
    return render_to_response('login.html', RequestContext(request))

def nuevoUsuario(request):
    if request.method=="POST":
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            nNombre = formulario.cleaned_data["nombre"]
            nApellidos = formulario.cleaned_data["apellidos"]
            nFechaNacimiento = formulario.cleaned_data["fechaNacimiento"]
            nSexo = formulario.cleaned_data["sexo"]
            nFoto = formulario.cleaned_data["profile"]
            nEmail = formulario.cleaned_data["email"]
            nPass = formulario.cleaned_data["password"]
            usuario = Usuario(nombre=nNombre, apellidos=nApellidos, fechaNacimiento=nFechaNacimiento, sexo=nSexo,profile=nFoto,email=nEmail,password=nPass)
            usuario.save()
            return HttpResponseRedirect("/")
    else:
        formulario = RegistroForm()
    return render_to_response('registro.html',{'formulario':formulario},context_instance=RequestContext(request))
            

