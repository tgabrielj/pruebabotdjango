import pandas as pd


#logica estrategia cruce de emas
def cruce_emas(dataframe):

	alcista = True
	cantidad_columnas = len(dataframe.columns)
	print("cantidad de columnas:",cantidad_columnas )
	periodos = [4,9,18]
	movimiento = "alcista"
	cumple_estrategia = False

	print("periodos desde cruce_emas: ", periodos)

	try:
		#nombre de la columna de menor periodo osea la primera la, posicion 1 , 0 es del precio de cierre
		nombre_columna = "EMA " + str(periodos[0])
		print("nombre columna EMA RAPIDA: ",nombre_columna)
		
		#ver si es alcista
		if alcista == True:
			# periodos indicadores 0 1 2 
			# columnas del data frame 0 1 2 3 a compara del data frame 2 3 
			for i in range(6,cantidad_columnas):
				#nombre de la siguiente columna a comparar
				nombre_sig_columna = "EMA " + str(periodos[i-1])
				print("nombre columna EMA SIGUIENTE: ",nombre_sig_columna)

				print(dataframe.iloc[-1][nombre_columna])
				print(dataframe.iloc[-1][nombre_sig_columna])



				#SI LA EMA RAPIDA ES MAYOR A TODAS LAS OTRAS, ES ALCISTA Y DEVUELVO MOVIMIENTO ALCISTA Y CUMPLE ESTRATEGIA Y NO HACE FALTA QUE VERIFIQUE LA ESTRATEGIA ES BAJISTA
				if (dataframe.iloc[-2][nombre_columna] > dataframe.iloc[-2][nombre_sig_columna]):
					alcista = True
					cumple_estrategia = True

				else:
					alcista = False
					cumple_estrategia = False
					movimiento = "bajista"
					break

			#input("VER VALORES")

		#ver si es bajista
		if alcista == False:
			# periodos indicadores 0 1 2 
			# columnas del data frame 0 1 2 3 a compara del data frame 2 3 
			for i in range(6,cantidad_columnas):
				#nombre de la siguiente columna a comparar
				nombre_sig_columna = "EMA " + str(periodos[i-1])

				#SI LA EMA RAPIDA ES MENOR A TODAS LAS OTRAS, ES BAJISTA Y DEVUELVO MOVIMIENTO BAJISTA Y CUMPLE ESTRATEGIA
				if (dataframe.iloc[-2][nombre_columna] < dataframe.iloc[-2][nombre_sig_columna]):

					cumple_estrategia = True

				else:
					cumple_estrategia = False
					movimiento = "nada"

					break

		return movimiento, cumple_estrategia

	except:
		"NO SE PUDO VERIFICAR LA ESTRATEGIA"