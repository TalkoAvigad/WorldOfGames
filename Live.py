from game import CurrencyRouletteGame as CurrencyRoulette, GuessGame, MemoryGame
import os


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    name = input('Please enter your name: ')
    clean()
    print('<====================================================>')
    print(f"Hello {name} and welcome to the World of Games (WoG). \n"
          "Here you can find many cool games to play.")
    print('<====================================================>')
    print('\n')
    input('Please press enter to continue.')
    clean()

def check_user_input(user_choose, first, last):
    if user_choose.isnumeric():
        user_choose = int(user_choose)

        if first <= user_choose <= last:
            return True, user_choose
        else:
            print(f"WRONG INPUT, Please enter number between {first}-{last}")
            return False, None
    else:
        print(f"WRONG INPUT, Please enter only number between {first}-{last}")
        return False, None


def load_game():
    choose_game = None
    choose_level = None
    check_input = False

    while not check_input:
        print("Please choose a game to play: \n"
              "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
              "2. Guess Game - guess a number and see if you chose like the computer \n"
              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
        print('\n')
        choose_game = input('Please enter your choose: ')
        clean()
        check_input, choose_game = check_user_input(choose_game, 1, 3)

    while check_input:
        choose_level = input("Please choose game difficulty from 1 to 5: ")
        clean()
        check_input, choose_level = check_user_input(choose_level, 1, 5)
        check_input = not check_input

    if choose_game == 1:
        MemoryGame.play(choose_level)
    if choose_game == 2:
        GuessGame.play(choose_level)
    if choose_game == 3:
        CurrencyRoulette.play(choose_level)

    clean()
