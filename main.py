from timer import countdown

def menuOptions():
    menu = {
        1: 'Timer App',
        2: 'Maybe a database related app',
        3: 'Perhaps a brev.dev project',
        4: 'Exit'
    }
    for key in menu.keys():
        print(key, f'--', menu[key])


def main():
    while(1):
        menuOptions()
        userInput = int(input(f'Choose option: '))
        if userInput == 1:
            userTime = input('Enter duration of timer in the following format: \n(hh:mm:ss): ')
            print(f'User input: ', userTime)
           # print(f'hh:mm:ss')
            countdown(userTime)
        elif userInput == 2:
            print(f'For future development')
        elif userInput == 3:
            print(f'Manifesting in the very near future a professional career like Mr Carter Abdallah aka baxate.')
        elif userInput == 4:
            print(f'Bye bye!!')
            exit(0)

#main()
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error: {}'.format(e))
