from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from principal.models import Usuario
from django.http import HttpResponseRedirect, HttpResponse
def index(request):
    return render_to_response('index.html')# Create your views here.
def login(request):
    if request.method=="POST":
        print request
        usuario = Usuario.objects.filter(username="")
    return render_to_response('login.html', RequestContext(request))