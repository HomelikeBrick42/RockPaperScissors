import random


# This function will repeatedly ask the
# user a question for a yes or no
#
# If the user says yes the function will return True
# If the user says no the function will return False
def ask_yes_no_question(question: str) -> bool:
    # Forever
    while True:
        # Ask the user for input
        # and strip the whitespace
        # and make all the characters lowercase
        answer: str = input(question).strip().lower()

        # If the user says "yes" or "y"
        if answer == "yes" or answer == "y":
            # Return out of the function and return True
            return True
        # If the user says "no" or "n"
        elif answer == "no" or answer == "n":
            # Return out of the function and return False
            return False
        # If the user answers with anything else
        else:
            # Continue the loop asking the user for an input
            print("Please enter yes or no")


# Displays the instructions
def show_instructions() -> None:
    print("No instructions are made right now")


def ask_user_rock_paper_scissors() -> chr:
    # Forever
    while True:
        # Ask the user for input and strip it of whitespace
        # and put it into lowercase
        answer: str = input("Enter rock (r), paper (p), or scissors (s), or (q) to quit ").strip().lower()

        # If the user inputs "rock" or "r"
        if answer == "rock" or answer == "r":
            # Return out of the function and return 'r'
            return 'r'
        # If the user inputs "paper" or "p"
        elif answer == "paper" or answer == "p":
            # Return out of the function and return 'p'
            return 'p'
        # If the user inputs "scissors" or "s"
        elif answer == "scissors" or answer == "s":
            # Return out of the function and return 's'
            return 's'
        # If the user inputs "gun"
        elif answer == "gun":
            # Print some messages
            print("You found the secret weapon!")
            print("[Computer]: You cheated :(")
            print("[Computer]: Goodbye")
            # Return the 0 character as a message to quit
            return '\0'
        # If the user inputs "quit" or "q"
        elif answer == "quit" or answer == "q":
            # Return the 0 character as a message to quit
            return '\0'
        # If the user answers with anything else
        else:
            # Continue the loop asking for an answer
            print("Please enter a valid answer\n")


def main() -> None:
    # Ask the user if they know how to play
    if not ask_yes_no_question("Do you know how to play? "):
        # Show the instructions
        show_instructions()

    # Newline for separation
    print()

    # Forever
    while True:
        # Ask the player for input
        player_answer: chr = ask_user_rock_paper_scissors()

        # If the answer is the quit character
        if player_answer == '\0':
            # Exit the main function
            return

        # Possible chances for the computer
        possible_answers: list[chr] = ['r', 'p', 's']
        # Make the computer chose a random answer
        computer_answer: chr = random.choice(possible_answers)

        # Maps the characters to strings
        answer_to_string: dict[chr, str] = {
            'r': "rock",
            'p': "paper",
            's': "scissors",
        }

        # Print what the player chose using the character to string map
        print(f"You chose {answer_to_string[player_answer]}")

        # Print what the computer chose using the character to string map
        print(f"The computer chose {answer_to_string[computer_answer]}")

        # Check for win or loose
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

        # Extra newline for separation
        print()


# If this file is not included as a module
if __name__ == "__main__":
    # Run the main function
    main()
