# Imports
import os
import random


# Main
def main():
    print("\nWelcome to the virtual game of Rock, Paper, Scissors, Shoot!")
    player = player_selection()
    computer = computer_selection()
    result(player, computer)


# Function for player selection
def player_selection():
    player_selection = input("Enter:\n- Rock\n- Paper\n- Scissors\n- Quit\n\n")
    os.system('cls')
    if player_selection.lower() == "quit":
        print("Thanks for playing!")
        exit()
    elif player_selection.lower() == "rock" or "paper" or "scissors":
        print(f"You selected: {player_selection.capitalize()}")
        return player_selection.lower()
    else:
        print(f"{player_selection} is not a valid entry.")
        main()


# Function for computer selection
def computer_selection():
    lst = ["Rock", "Paper", "Scissors"]
    computer_selection = random.choice(lst)
    print(f"Computer selected: {computer_selection}")
    return computer_selection.lower()


# Function to determine result
def result(player, computer):
    if player == computer:
        print("Result - Tie")
        post_result()
    elif player == "rock" and computer =="scissors":
        print("Rock Crushes Scissors.\nResult - YOU WON!")
        post_result()
    elif player == 'paper' and computer == "rock":
        print("Paper Covers Rock.\nResult - YOU WON!")
        post_result()
    elif player == 'scissors' and computer == "paper":
        print("Scissors Cuts Paper.\nResult - YOU WON!")
        post_result()
    elif player == "rock" and computer == "paper":
        print("Paper Covers Rock.\nResult - Computer Wins.")
        post_result()
    elif player == "paper" and computer == "scissors":
        print("Scissors Cuts Paper.\nResult - Computer Wins.")
        post_result()
    elif player == "scissors" and computer == "rock":
        print("Rock Crushes Scissors.\nResult - Computer Wins.")
        post_result()


# Function to run after there has been a result
def post_result():
    print("\nThanks for playing! Please play again!")
    main()


main()