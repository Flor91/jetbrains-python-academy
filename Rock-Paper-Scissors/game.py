import math
import random

OPTIONS_ORIGINAL = ["rock", "paper", "scissors"]
# rock,paper,scissors,lizard,spock
# rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire

FILENAME = "rating.txt"


def get_options():
    user_selected_options = input().strip()
    options = user_selected_options.split(",")
    if len(options) > 3:
        return options
    return OPTIONS_ORIGINAL


def load_user_ratings():
    file = open(FILENAME, "r")
    ratings = {}
    for line in file.readlines():
        name, rating = line.split(" ")
        ratings[name] = int(rating)
    file.close()
    return ratings


def save_ratings(user_ratings):
    file = open(FILENAME, "w")
    for name, rate in user_ratings.items():
        print(name, rate)
        file.write("{} {}\n".format(name, rate))
    file.close()


def is_user_winner(options, user_choice, computer_choice):
    number_winners = math.floor(len(options) / 2)
    user_index = options.index(user_choice)

    ordered_chosen_options = options[user_index + 1:] + options[:user_index]
    user_wins = ordered_chosen_options[number_winners:]

    return computer_choice in user_wins


username = input("Enter your name: ").strip()
print("Hello, " + username)

user_ratings = load_user_ratings()

if username not in user_ratings:
    user_ratings[username] = 0

options = get_options()

print("Okay, let's start")

computer = random.choice(options)
user_option = input()

while user_option != "!exit":
    if user_option not in options:
        if user_option == "!rating":
            print("Your rating: " + str(user_ratings[username]))
        else:
            print("Invalid input")
    else:
        if user_option == computer:
            user_ratings[username] += 50
            print("There is a draw " + user_option)
        elif is_user_winner(options, user_option, computer):
            user_ratings[username] += 100
            print("Well done. Computer chose {option} and failed".format(option=computer))
        else:
            print("Sorry, but the computer chose {option}".format(option=computer))

    computer = random.choice(options)
    user_option = input()

save_ratings(user_ratings)

print("Bye!")
