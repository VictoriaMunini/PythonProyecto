from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppMunini.models import Familiares

def listadoFamiliares(request):

    listaFamilia = Familiares.objects.all()
    data = {
        "listaFamilia": listaFamilia,

    }

    plantilla = loader.get_template("Template.html")
    
    documento =  plantilla.render(data)
    
    return HttpResponse(documento)


