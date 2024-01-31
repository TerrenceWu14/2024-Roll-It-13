import random


# Performs a single dice roll
def roll_die():
    result = random.randint(1, 6)
    return result


# Performs a double roll and tells us if they're a pair or not
def double_roll():
    double_score = "no"

    # Rolls two dice (First rolls)
    roll_1 = roll_die()
    roll_2 = roll_die()
    # Checks if it's possible to double the score

    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points after the first dice roll
    user_points = roll_1 + roll_2

    # Shows the result of the dice rolls
    return user_points, double_score


# Main routine goes here
print("Press <enter> to begin this round: ")
input()
# Gets the initial points for the user
user_first = double_roll()
user_points = user_first[0]
double_points = user_first[1]
# Tells the user if they are eligible for double points
if double_points == "no":
    double_message = ""
elif double_points == "yes":
    double_message = "You are also eligible to win double the points if you win this round!"

# Displays the first moves results
print(f"You managed to get {user_points}. {double_message}")

# Gets initial dice rolls for computer
computer_first = double_roll()
computer_points = computer_first[0]
double_points = computer_first[1]

# Displays the amount of points the computer got
print(f"The computer got {computer_points}")

# While both the user and the computer have <= points it keeps looping
while user_points <= 13 and computer_points <= 13:
    roll_again = input("Press <enter> to roll again or any letter to pass your turn: ")
    # Rolls a single die
    if roll_again == "":
        user_roll_again = roll_die()
        # Adds what you got from the roll onto your current points
        user_points += user_roll_again
        # Displays what you rolled and your new updated points
        print(f"You rolled a {user_roll_again}. Total points: {user_points}")
    else:
        print("You passed your turn")
        break
    # Rolls a single die
    computer_roll_again = roll_die()
    # Adds what you got from the roll onto your current points
    computer_points += computer_roll_again
    # Displays what the computer rolled and the new updated points
    print(f"The Computer rolled a {computer_roll_again}. Total points: {computer_points}")
