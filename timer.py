import time

def parseTime(userTime):
    parsedTime = {}
    if len(userTime) == 8:
        parsedTime = {
            'hours': userTime.split(':')[0],
            'minutes': userTime.split(':')[1],
            'seconds': userTime.split(':')[2]
        }
    elif len(userTime) == 5:
        parsedTime = {
            'minutes': userTime.split(':')[0],
            'seconds': userTime.split(':')[1]
        }
    elif len(userTime) <= 2:
        if(len(userTime) == 1):
            parsedTime = {
                'hours': '0' + userTime[0]
            }
        else:
            parsedTime = {
                'hours': userTime[0]
            }
    return parsedTime

#print(parseTime('01:01:01'))
#print(len(parseTime('01:01:01')))
print("If I can see this from main then python executes files when imported before they're even called")

def countdown(time):
    parsedTime = parseTime(time)
    timeInSeconds = int((parsedTime['hours'] * 3600) + (parsedTime['minutes'] * 60) + (parsedTime['seconds']))

    while(timeInSeconds > 0 ):
        hours = timeInSeconds // 3600
        minutes = (timeInSeconds % 3600) // 60
        seconds = timeInSeconds % 60
        time_format = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
        print(time_format)
        time.sleep(1)
        timeInSeconds -= 1
    if timeInSeconds == 0:
        print(f'---Time is up---')
