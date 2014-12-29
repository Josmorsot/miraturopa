from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
def index(request):
    return render_to_response('index.html')# Create your views here.
