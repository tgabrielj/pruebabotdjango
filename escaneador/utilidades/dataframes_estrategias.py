from tvDatafeed import TvDatafeed, Interval as inter
import pandas as pd
from .indicadores import *

def obtener_dataframe_historial(exchange, ticker, intervalo):
	try:

		tv = TvDatafeed()

		#primero va el simbolo y luego el exchange
		price_data = tv.get_hist(ticker,exchange, intervalo , n_bars=1000)

		return price_data

	except:

		print("no se puedo obtener los datos de tradingview")

		return None
	
# genera el dataframe requerido para verificar las condiciones de la estrategia
def dataframe_estrategia_cruce_emas(exchange, ticker, intervalo):

	print("IMPRIMO TIKCER QUE LLEGA A FUNCION indicadores: ", ticker)
	# bandera con resultado de armado del dataframe con los indicadores
	operacion = True

	lista_periodos = [4,9,18]

	try:

		dataframe = obtener_dataframe_historial(exchange, ticker, intervalo)


		for i in range(len(lista_periodos)):
			#nombre_columna = str('EMA ' + str(lista_periodos[i]) )
			#dataframe[nombre_columna] = pd.Series( ema(periodos[i] , precios_cierre), index=dataframe.index )
			ema(lista_periodos[i],dataframe)

		print(dataframe)
		return dataframe

	except:
		print("no se pudo armar el dataframe con todas las emas")
		operacion = False
		return operacion
