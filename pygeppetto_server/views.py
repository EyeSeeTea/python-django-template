from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello, world. You're at the pygeppetto_server index.")
    return render(request, 'org.geppetto.frontend/src/main/webapp/build/geppetto.vm', {})