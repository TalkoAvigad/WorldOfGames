import random


def generate_number(big_number_random):
    random_number = random.randint(1, big_number_random)
    return random_number


def get_guess_from_user(big_number_guess):
    check_input = False

    while not check_input:
        user_guess_numer = input(f"Please guess number between 1-{big_number_guess}: ")

        if user_guess_numer.isnumeric():
            user_guess_numer = int(user_guess_numer)

            if 1 <= user_guess_numer <= big_number_guess:
                return user_guess_numer
            else:
                print(f"WRONG INPUT, Please enter number between 1-{big_number_guess}")
        else:
            print(f"WRONG INPUT, Please enter only number between 1-{big_number_guess}")


def compare_results(secret_number, guess_numer):
    if secret_number == guess_numer:
        return True
    else:
        False


def play(level):
    secret_number = generate_number(level)
    guess_numer = get_guess_from_user(level)

    if compare_results(secret_number, guess_numer):
        print("You guessed the number correctly and won the game!!!")
        input('\nPlease press enter to continue.')
        return True
    else:
        print(f"Too bad you couldn't guess the number, the correct number was {secret_number}. \n"
              f"Good luck in the next round ")
        input('\nPlease press enter to continue.')
        return False
