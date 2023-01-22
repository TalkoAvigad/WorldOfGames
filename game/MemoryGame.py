import Live
import random
import time


def generate_sequence(length_random_list):
    random_list = []
    for i in range(0, length_random_list):
        random_number = random.randint(1, 101)
        random_list.append(random_number)
    return random_list


def get_list_from_user(length_guess_list):
    guess_list = []
    len_guess_list_full = False
    while not len_guess_list_full:
        user_guess_list_numer = input(f"Please guess a list of length {length_guess_list} of the numbers 1-101," 
                                      f" You have to guess {length_guess_list-len(guess_list)} more numbers: ")

        if user_guess_list_numer.isnumeric():
            user_guess_list_numer = int(user_guess_list_numer)

            if 1 <= user_guess_list_numer <= 101:
                guess_list.append(user_guess_list_numer)
                if len(guess_list) == length_guess_list:
                    len_guess_list_full = True
            else:
                print("WRONG INPUT, Please enter number between 1-101")
        else:
            print("WRONG INPUT, Please enter only number between 1-101")

    return guess_list


def is_list_equal(random_secret_number, guess_list_by_user):
    if random_secret_number == guess_list_by_user:
        return True
    else:
        return False


def play(level):
    secret_list_number = generate_sequence(level)
    print(secret_list_number)
    time.sleep(0.7)
    Live.screen_cleaner()

    guess_list_numer = get_list_from_user(level)
    if is_list_equal(secret_list_number, guess_list_numer):
        print("You guessed the list of numbers correctly and won the game!!!")
        input('\nPlease press enter to continue.')
        return True
    else:
        print(f"Too bad you couldn't guess the list of numbers, the correct numbers was {secret_list_number}. \n"
              f"Good luck in the next round ")
        input('\nPlease press enter to continue.')
        return False
