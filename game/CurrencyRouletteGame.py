import random
import urllib.request as req
import json


def get_money_interval(difficulty_level):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = req.urlopen(url)
    data = json.load(response)
    exchange_rates = (data['rates'])
    exchange_rates_ILS = float(exchange_rates['ILS'])
    print(exchange_rates_ILS)
    random_value_USD_money = random.randint(1, 100)
    USD_to_ILS = random_value_USD_money * exchange_rates_ILS
    interval_range = (USD_to_ILS - (5 - difficulty_level), USD_to_ILS + (5 - difficulty_level))
    return random_value_USD_money, USD_to_ILS, interval_range


def get_guess_from_user(USD):
    while True:
        user_guess_numer = input(f"Guess the conversion from {USD}$ to ₪: ")

        if user_guess_numer.isnumeric():
            user_guess_numer = int(user_guess_numer)
            return user_guess_numer
        else:
            print(f"WRONG INPUT, Please enter only number")


def play(difficulty):
    USD, ILS, interval = get_money_interval(difficulty)
    user_guess = get_guess_from_user(USD)
    if user_guess == ILS:
        print('You guessed exactly the conversion from $ to ₪ and won the game!!!')
        input('\nPlease press enter to continue.')
        return True
    elif interval[0] <= user_guess <= interval[1]:
        print(f"You have guessed in the range {interval} the conversion from $ to ₪ correctly and won the game!!!")
        input('\nPlease press enter to continue.')
        return True
    else:
        print(f"Too bad you couldn't guess the conversion from $ to ₪, Good luck in the next round ")
        input('\nPlease press enter to continue.')
        return False
