# Checks whether the user entered yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response to question
        # repeats itself if the user types invalid option
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You didn't choose a valid option (yes/no)")
            print()


# Displays instructions
def instructions():
    print('''

*** Instructions ***

To begin, you decide on a score goal (e.g The first to get 50 points (or higher))

For each round of the games you roll a dice to decide how many points you get
The winner of the round is the person who is the closest to 13 (must not be higher)

If you win the round then your score will increase by the number you got,
If you were to roll a double on your first oll (e.g. 2 6s) 
then you gain DOUBLE the amount of points (12 x 2 = 24)

If you lose the round you gain 0 points

If there is a tie then both players get the same number of points added 
For example - You roll 11 and the Computer rolls 11, this means you both gain 11 points

Your goal is to get the target score (or higher) first before the Computer does

    ''')


# Checks that the user has entered an integer
def num_check():
    error = "Please choose an integer that is 13 or greater"

    # Checks that a number is higher or equal to 13
    try:
        response = int(input("Enter an Integer: "))
        if response < 13:
            print(error)
        else:
            return response
    except ValueError:
        print(error)


# Main Routine
# Displays the title
print()
print("🎲🎲🎲 Roll It 13 🎲🎲🎲")
print()

# Loops the code

want_instruction = yes_no("Do you want to read the instructions? (If so type yes or if not type no)")

# Checks whether the user entered yes or no
if want_instruction == "yes" or want_instruction == "y":
    instructions()

print()
target_score = num_check()
print(target_score)
