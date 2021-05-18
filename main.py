from typing import List, Dict

import random


def ask_yes_no_question(question: str) -> bool:
    while True:
        answer: str = input(question).strip().lower()

        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Please enter yes or no")


def show_instructions() -> None:
    print("No instructions are made right now")


def main() -> None:
    if not ask_yes_no_question("Do you know how to play? "):
        show_instructions()

    print()

    while True:
        player_answer: chr = '\0'

        while True:
            answer: str = input("Enter rock (r), paper (p), or scissors (s), or (q) to quit ").strip().lower()

            if answer == "rock" or answer == "r":
                player_answer = 'r'
                break
            elif answer == "paper" or answer == "p":
                player_answer = 'p'
                break
            elif answer == "scissors" or answer == "s":
                player_answer = 's'
                break
            elif answer == "gun":
                print("You found the secret weapon!")
                print("[Computer]: You cheated :(")
                print("[Computer]: Goodbye")
                return
            elif answer == "quit" or answer == "q":
                return
            else:
                print("Please enter a valid answer\n")

        possible_answers: List[chr] = ['r', 'p', 's']
        answer_to_string: Dict[chr, str] = {
            'r': "rock",
            'p': "paper",
            's': "scissors",
        }

        computer_answer: chr = random.choice(possible_answers)
        print(f"You chose {answer_to_string[player_answer]}")
        print(f"The computer chose {answer_to_string[computer_answer]}")

        if player_answer == 'r':
            if computer_answer == 'r':
                print("Tie!")
            elif computer_answer == 'p':
                print("You loose!")
            elif computer_answer == 's':
                print("You win!")
        elif player_answer == 'p':
            if computer_answer == 'r':
                print("You win!")
            elif computer_answer == 'p':
                print("Tie!")
            elif computer_answer == 's':
                print("You loose!")
        elif player_answer == 's':
            if computer_answer == 'r':
                print("You loose!")
            elif computer_answer == 'p':
                print("You win!")
            elif computer_answer == 's':
                print("Tie!")

        print()


if __name__ == "__main__":
    main()
