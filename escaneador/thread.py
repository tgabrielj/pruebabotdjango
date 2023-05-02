import threading
from .models import *
import time
from django.shortcuts import get_object_or_404
#from tvDatafeed import Interval as inter

from .utilidades.tvDatafeed import Interval as inter
from .utilidades.dataframes_estrategias import *
from .utilidades.estrategias import *

from faker import Faker
fake = Faker()

import random

class CreateStudentsThread(threading.Thread):
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            print('Thread execution started')
            for i in range(self.total):
                print(i)
                Students.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10,50)
                )
                time.sleep(5)
            print("FIN")
        except Exception as e:
            print(e)

class CreateEscaneadorThread(threading.Thread):

    def __init__(self, escaneador):

        self.escaneador = escaneador
        threading.Thread.__init__(self)
        
    def run(self):

        #escaneador = Escaneador.objects.create(
         #           en_ejecucion = True,
         #           estrategia = "CRUCE DE EMAS"
         #       )
        try:
            print('Escaneador activado')
            while self.escaneador.en_ejecucion == True:
                print("ANALIZANDO")
                time.sleep(5)
                print(self.escaneador.get_estrategia())

                self.escaneador = get_object_or_404(Escaneador, pk = self.escaneador.id)
                print(self.escaneador.id)

            print("FIN - SE DESACTIVO EL BOT")
        except Exception as e:
            print(e)

class EstrategiaCruceEmasThread(threading.Thread):

    def __init__(self, escaneador):

        self.escaneador = escaneador
        threading.Thread.__init__(self)
        
    def run(self):

        #escaneador = Escaneador.objects.create(
         #           en_ejecucion = True,
         #           estrategia = "CRUCE DE EMAS"
         #       )

        try:

            alertas = []

            while self.escaneador.en_ejecucion == True:
                
                dataframe_estrategia = dataframe_estrategia_cruce_emas("BINGX","SOLUSDT.PS", inter.in_1_minute)
                indice_dataframe_intervalo_seleccionado = dataframe_estrategia.index

                #operacion = Operacion.objects.create(
                 #       id_escaneador = self.escaneador.id,
                  #      nombre_estrategia = self.escaneador.estrategia,
                   #     fecha = str(indice_dataframe_intervalo_seleccionado[-2]),
                    #    precio_entrada = str(dataframe_estrategia.iloc[-2]["close"])
                    #)

                #alcista
                if dataframe_estrategia.iloc[-1]["EMA 4"] > dataframe_estrategia.iloc[-1]["EMA 9"] and dataframe_estrategia.iloc[-1]["EMA 4"] > dataframe_estrategia.iloc[-1]["EMA 18"] and (dataframe_estrategia.iloc[-2]["EMA 4"] < dataframe_estrategia.iloc[-2]["EMA 9"] or dataframe_estrategia.iloc[-2]["EMA 4"] < dataframe_estrategia.iloc[-2]["EMA 18"]):
                     
                     if indice_dataframe_intervalo_seleccionado not in alertas:

                        alertas.append(indice_dataframe_intervalo_seleccionado)
                     #crear objeto operacion y guardar en base de datos
                        operacion = Operacion.objects.create(
                            id_escaneador = self.escaneador.id,
                            nombre_estrategia = self.escaneador.estrategia,
                            fecha = str(indice_dataframe_intervalo_seleccionado[-2]),
                            precio_entrada = str(dataframe_estrategia.iloc[-2]["close"]),
                            movimiento = "LONG"
                        )
                
   
                # bajista
                if dataframe_estrategia.iloc[-1]["EMA 4"] < dataframe_estrategia.iloc[-1]["EMA 9"] and dataframe_estrategia.iloc[-1]["EMA 4"] < dataframe_estrategia.iloc[-1]["EMA 18"] and (dataframe_estrategia.iloc[-2]["EMA 4"] > dataframe_estrategia.iloc[-2]["EMA 9"] or dataframe_estrategia.iloc[-2]["EMA 4"] > dataframe_estrategia.iloc[-2]["EMA 18"]):
                     
                     #crear objeto operacion y guardar en base de datos
                     if indice_dataframe_intervalo_seleccionado not in alertas:
                        
                        alertas.append(indice_dataframe_intervalo_seleccionado)
                     #crear objeto operacion y guardar en base de datos
                        operacion = Operacion.objects.create(
                            id_escaneador = self.escaneador.id,
                            nombre_estrategia = self.escaneador.estrategia,
                            fecha = str(indice_dataframe_intervalo_seleccionado[-2]),
                            precio_entrada = str(dataframe_estrategia.iloc[-2]["close"]),
                            movimiento = "SHORT"
                        )
                

                #print("ANALIZANDO")
                #time.sleep(5)
                #print(self.escaneador.get_estrategia())

                #print(movimiento, cumple_estrategia)
                print(dataframe_estrategia)
                time.sleep(5)

                self.escaneador = get_object_or_404(Escaneador, pk = self.escaneador.id)
                print(self.escaneador.id)

            print("FIN - SE DESACTIVO EL BOT")

        except Exception as e:
            print(e)