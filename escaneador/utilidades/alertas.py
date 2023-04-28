import pygame
import requests

def alerta_sonido(var_check_sonido):
	pygame.mixer.init()
	if var_check_sonido == True:
		pygame.mixer.music.load("./utilidades/alert_sound.mp3")
		pygame.mixer.music.play(loops=0)
	
	else:
		print("no se emitio sonido de alerta")


def telegram_bot_sendtext(bot_message, var_check_telegram):

	if var_check_telegram == True:
		bot_token = '1469558221:AAGsa9-DcabRhN7d4Mle0KZzcFwKdNeWgnk'
		bot_chatID = '1322419572'
	
		send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

		requests.get(send_text)

	else:
		print("no se envio el alerta por telegram")
