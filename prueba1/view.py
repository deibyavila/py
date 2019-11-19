

from django.http import HttpResponse
#from django.http import JsonResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('XXhellow world!! WTF  {now}'.format(now=now))



def valu(request, name, edad):
    if edad < 12:
        message = 'lo sisneto {0} es menor de 12'.format(name)
    else:
        message = 'bienvenido {0}, tienes {1}'.format(name,edad)
    return HttpResponse(message)


def hola(request):
    jsonlista = {}
    lista = request.GET['numero']
    try:
        #import pdb; pdb.set_trace()
        jsonlista = [int(x) for x in lista.split(',')]
        ordenada = sorted(jsonlista)
        print(lista)
        
        data = {
            'status' : 'ok',
            'number' : ordenada,
            'message' : 'Lista de Integrales ordenada'
        }
        response = data
    except Exception as e:
        print(type(e).__name__)
        response = {'mensaje':'error'}

    finally:
        return HttpResponse(
            json.dumps(response)
            , content_type='application/json'
            )

