import time
from playsound import playsound

def parseTime(userTime):
    newTime = userTime.split(':')
    parsedTime = {}
    if len(newTime) == 3:
        parsedTime = {
            'hours': int(newTime[0]),
            'minutes': int(newTime[1]),
            'seconds': int(newTime[2])
        }
    if len(newTime) == 2:
        parsedTime = {
            'minutes': int(newTime[0]),
            'seconds': int(newTime[1])
        }
    if len(newTime) == 1:
        parsedTime = {
            'seconds': int(newTime[0])
        }
    return parsedTime

#print(parseTime('01:01:01'))
#print(len(parseTime('01:01:01')))
#print("If I can see this from main then python executes files when imported before they're even called")

def countdown(userTime):
    parsedTime = parseTime(userTime)
    timeInSeconds = (parsedTime['hours'] * 3600) + (parsedTime['minutes'] * 60) + (parsedTime['seconds'])

    while(timeInSeconds > 0 ):
        hours = timeInSeconds // 3600
        minutes = (timeInSeconds % 3600) // 60
        seconds = timeInSeconds % 60
        time_format = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
        print(time_format)
        time.sleep(1)
        timeInSeconds -= 1
    if timeInSeconds == 0:
        print('\033[1;30;41m---Time is up---\033[0m\n')
        playsound('alarm-clock-loop-90916.wav')
