import sys, os
parentDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parentDir)
### Allows to include other directorys and treat them as modules

from Timer.timer import countdown

def menuOptions():
    menu = {
        1: '\033[1;30;45mTimer App\033[0m',
        2: '\033[1;30;46mMaybe a database related app\033[0m',
        3: '\033[1;30;42mMusic Genre Classifier\033[0m',
        4: '\033[1;30;41mExit\033[0m'
    }
    for key in menu.keys():
        print(key, f'--', menu[key])


def main():
    while(1):
        print('\033[1;30;44mA bundled toolkit of some projects of mine.\033[m\n')
        menuOptions()
        userInput = int(input('Choose option: '))
        if userInput == 1:
            userTime = input('Enter duration of timer in the following format: \n(hh:mm:ss): ')
            print(f'User input: ', userTime)
           # print(f'hh:mm:ss')
            countdown(userTime)
        elif userInput == 2:
            print('For future development\n')
        elif userInput == 3:
            print('Manifesting in the very near future a professional career like Mr Carter Abdallah aka baxate.\n')
        elif userInput == 4:
            print('Bye bye!!')
            exit(0)

#main()
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error: {}'.format(e))
