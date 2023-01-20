from django.http import HttpResponse
import datetime


def home(request):
    return HttpResponse('<h1>HOLA MUNDO</h1>')

def inicio(request):
    hoy = datetime.datetime.now()
    return HttpResponse('Hoy es %s/%s/%s y son las %s:%s de la tarde'%(hoy.day,hoy.month,hoy.year,hoy.hour,hoy.minute))

def iva(request,cant,precio):
    iva= 1.21
    pvp = precio*iva
    total= pvp*cant
    return HttpResponse("El precio total para %s unidades, es de: %s " %(cant,total))