from Live import welcome, load_game
from Utils import screen_cleaner

welcome()

while True:
    load_game()

    print('Do you want to play another round?')
    answer = input('Press [Y/y] for yes, to exit press any key: ')

    if answer == 'Y' or answer == 'y':
        screen_cleaner()
    else:
        exit()
