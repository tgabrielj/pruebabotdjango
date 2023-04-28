import pandas as pd

def ema(periodo, dataframe):
	ema_periodo = 'EMA ' + str(periodo)
	
	dataframe[ema_periodo] = dataframe['close'].ewm(span=periodo, adjust=False).mean()
