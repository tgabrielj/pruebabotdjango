from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from faker import Faker
from .forms import EscaneadorForm
fake = Faker()
import random
from .thread import CreateStudentsThread, CreateEscaneadorThread, EstrategiaCruceEmasThread

from .utilidades.dataframes_estrategias import *
from .utilidades.tvDatafeed import Interval as inter



# Create your views here.

def dashboard(request):
    count = 100
    CreateStudentsThread(count).run()

    context = {'result' : 'Your task is started'}
    return render(request, 'dashboard.html', context)

def home(request):
    return render(request, 'home.html')


def escanear(request):

    CreateEscaneadorThread().start()

    return render(request, 'dashboard.html')

def escaneadores(request):
    escaneadores = Escaneador.objects.filter()
    #print(escaneadores)
    return render(request, 'escaneadores.html', {'escaneadores': escaneadores})


def escaneador_activar(request, escaneador_id):
    escaneador = get_object_or_404(Escaneador, pk = escaneador_id)
    if request.method == 'POST':
        escaneador.en_ejecucion = True
        escaneador.save()

        #print(obtener_dataframe_historial("BINGX","SOLUSDT.PS", inter.in_5_minute ))

        #dataframe_estrategia = dataframe_estrategia_cruce_emas("BINGX","SOLUSDT.PS", inter.in_5_minute )

        EstrategiaCruceEmasThread(escaneador).start()

        return redirect('escaneadores')
    
def escaneador_desactivar(request, escaneador_id):
    escaneador = get_object_or_404(Escaneador, pk = escaneador_id)
    if request.method == 'POST':
        escaneador.en_ejecucion = False
        escaneador.save()
        return redirect('escaneadores')
    
def ver_operaciones(request, escaneador_id):
        
        operaciones = Operacion.objects.filter()

        return render(request, 'ver_operaciones.html', {'escaneador_id':escaneador_id ,'operaciones': operaciones})
    
def create_escaneador(request):
    if request.method == 'GET':
        return render(request, 'create_escaneador.html', {
            'form': EscaneadorForm
        })
    else:
        try:
            form = EscaneadorForm(request.POST)
            new_task = form.save(commit = False)
            new_task.user = request.user
            new_task.save()
            return redirect('escaneadores')
        except ValueError:
            return render(request, 'create_escaneador.html', {
                'form': EscaneadorForm,
                'error': 'Plase provide valid data'
            })


#def escaneadores_activados(request):
 #   tasks = Task.objects.filter(user=request.user, datecompleted__isnull = False).order_by('-datecompleted')
  #  return render(request, 'tasks.html', {'tasks': tasks})