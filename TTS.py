import os
import winsound

message = ""
def speak(message):
	if "/" in message:
		if message[1:]=="evillaugh":
			winsound.PlaySound('C:\\Users\\craz0\\Desktop\\Programing\\Geany\\TTS\\laugh.wav', winsound.SND_FILENAME)
		if message[1:]=="scream":
			winsound.PlaySound('C:\\Users\\craz0\\Desktop\\Programing\\Geany\\TTS\\scream.wav', winsound.SND_FILENAME)
	
	else:
		if message=="":
			message = '"Your message is empty"'
		os.system("C:\\Users\\craz0\\Desktop\\Programing\\Geany\\TTS\\TTS.vbs "+'"'+message+'"')
