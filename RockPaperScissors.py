import random
import os
import time

def get_user_choice():
    # Prompts the user for their choice and validates it
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def get_computer_choice():
    # Generates a random choice for the computer.
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    # Determines the winner
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"


def display_result(user_choice, computer_choice, winner, scores):
    # Displays the choices, result, and current scores.
    print(f"\nYour choice: {user_choice.capitalize()}")

    print(f"Computer's choice: {computer_choice.capitalize()}")

    if winner == "tie":
        print("\nIt's a tie! �")
    elif winner == "user":
        print("\nYou win! 🎉")
    else:
        print("\nYou lose! 😢")

    print("-" * 20)
    print(f"Score -> You: {scores['user']} | Computer: {scores['computer']}")
    print("-" * 20)


def play_game():
    scores = {"user": 0, "computer": 0}

    while True:
        print("==============================")
        print(" Rock, Paper, Scissors Game ")
        print("==============================")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("\nRock...")
        time.sleep(0.7)
        print("Paper...")
        time.sleep(0.7)
        print("Scissors...")
        time.sleep(0.7)
        print("Shoot!")
        time.sleep(0.3)

        winner = determine_winner(user_choice, computer_choice)

        # Update scores
        if winner == "user":
            scores["user"] += 1
        elif winner == "computer":
            scores["computer"] += 1

        display_result(user_choice, computer_choice, winner, scores)

        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == "no":
            print("\nThanks for playing! Final score:")
            print(f"You: {scores['user']} | Computer: {scores['computer']}")
            break


if __name__ == "__main__":
    play_game()