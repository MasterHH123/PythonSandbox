def parseTime(userTime):
    parts = userTime.split(' ')
    parsedTime = {
        'hours': parts[0].split(':')[0],
        'minutes': parts[1].split(':')[1],
        'seconds': parts[2].split(':')[2]
    }
    return parsedTime
#parseTime only works when input time isn't in seconds, obviously'

def countdown(time):
    return print(f'Only a test to see if import works for now.')
