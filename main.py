from art import logo, vs
from data import data
import random

def format_data(acc):
    acc_name = acc["name"]
    acc_descr = acc["description"]
    acc_country = acc["country"]
    return f"{acc_name}, a {acc_descr}, from {acc_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
continue_game = True

acc_b = random.choice(data)

while continue_game:
    acc_a = acc_b
    acc_b = random.choice(data)

    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Compare A: {format_data(acc_a)}.")
    print(vs)
    print(f"Against B: {format_data(acc_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = acc_a["follower_count"]
    b_follower_count = acc_b["follower_count"]
    correct = check_answer(guess, a_follower_count, b_follower_count)

    print(logo)

    if correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}.")
