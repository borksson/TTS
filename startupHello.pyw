import random
from time import time, gmtime, localtime, strftime
import TTS

random.seed(int(time()))
TSFileName = "TSFile.txt"
time = strftime("{%d:%H}", localtime())
TSFile = open(TSFileName, "r+")
TSFileData = TSFile.read()
lastStamp = TSFileData[len(TSFileData)-7:len(TSFileData)]
timeBuffer = 0
TSFile.write(time)
TSFile.close()
messages = []
phrasesFile = open("phrases.txt", "r")
for i in phrasesFile:
	messages.append(i)
message = random.choice(messages)
if int(time[1:3]) == int(lastStamp[1:3]):
	if int(time[4:6]) >= int(lastStamp[4:6])+timeBuffer:
		dayState = "Good morning,"
		if int(time[4:6])>= 19:
			dayState = "Evening,"
		elif int(time[4:6])>=12:
			dayState = "Afternoon, "
		TTS.speak(dayState + "Maxwell." + " " + message)

else:
	if int(time[4:6])+23 >= int(lastStamp[4:6])+timeBuffer:
		dayState = "Good morning,"
		if int(time[4:6])>= 19:
			dayState = "Evening,"
		elif int(time[4:6])>=12:
			dayState = "Afternoon, "
		TTS.speak(dayState + " " + "Maxwell." + " " + message)

