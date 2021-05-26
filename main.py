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


def ask_user_rock_paper_scissors() -> chr:
    while True:
        answer: str = input("Enter rock (r), paper (p), or scissors (s), or (q) to quit ").strip().lower()

        if answer == "rock" or answer == "r":
            return 'r'
        elif answer == "paper" or answer == "p":
            return 'p'
        elif answer == "scissors" or answer == "s":
            return 's'
        elif answer == "gun":
            print("You found the secret weapon!")
            print("[Computer]: You cheated :(")
            print("[Computer]: Goodbye")
            return '\0'
        elif answer == "giganotosaurus" or answer == "giga":
            print("[Computer]: Ahhhhhhhhhhh")
            print("Crunch...")
            return '\0'
        elif answer == "quit" or answer == "q":
            return '\0'
        else:
            print("Please enter a valid answer\n")


def main() -> None:
    if not ask_yes_no_question("Do you know how to play? "):
        show_instructions()

    print()

    while True:
        player_answer: chr = ask_user_rock_paper_scissors()

        if player_answer == '\0':
            return

        possible_answers: list[chr] = ['r', 'p', 's']
        computer_answer: chr = random.choice(possible_answers)

        answer_to_string: dict[chr, str] = {
            'r': "rock",
            'p': "paper",
            's': "scissors",
        }

        print(f"You chose {answer_to_string[player_answer]}")
        print(f"The computer chose {answer_to_string[computer_answer]}")

        win: dict[chr, chr] = {
            'r': 's',
            'p': 'r',
            's': 'p',
        }

        loose: dict[chr, chr] = {
            'r': 'p',
            'p': 's',
            's': 'r',
        }

        if win[player_answer] == computer_answer:
            print("You won!")
        elif loose[player_answer] == computer_answer:
            print("You loose!")
        else:
            print("Tie!")

        print()


if __name__ == "__main__":
    main()
