import random


# Performs a single dice roll
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# Performs a double roll and tells us if they're a pair or not
def double_roll(who):
    double_score = "no"

    # Rolls two dice (First rolls)
    roll_1 = roll_die()
    roll_2 = roll_die()
    # Checks if it's possible to double the score

    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points after the first dice roll
    first_points = roll_1 + roll_2

    # Prints out who got how many points and what they got from their rolls
    print(f"{who} managed to get {roll_1} and {roll_2}. Total Points: {first_points}")

    # Shows the result of the dice rolls
    return first_points, double_score


# Main routine goes here
print("Press <enter> to begin this round (roll the dies): ")
input()
# Gets the initial points for the user
user_first = double_roll("You")
user_points = user_first[0]
double_points = user_first[1]
# Tells the user if they are eligible for double points
if double_points == "no":
    double_message = ""
elif double_points == "yes":
    double_message = ("You are also eligible to win double the points"
                      " if you win this round since you got a pair!")

# Gets initial dice rolls for computer
computer_first = double_roll("Computer")
computer_points = computer_first[0]
double_points = computer_first[1]

# While both the user and the computer have <= points it keeps looping
while user_points < 13 and computer_points < 13:
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
    # Checks to see whether the user or computer have goner over 13 or not
    if user_points > 13:
        # Makes it so that the loser gets this rounds' points reset to 0
        user_points = 0
        break
    print()

    # Rolls the die for the computer and updates its points
    computer_roll_again = roll_die()
    computer_points += computer_roll_again
    print(f"The Computer rolled a {computer_roll_again}. Total points: {computer_points}")

    if computer_points > 13:
        computer_points = 0
        break

    print()
    # If user points > computer points it tells you that you're ahead
    if user_points > computer_points:
        result = "You are ahead"
    else:
        result = "The Computer is ahead"
    # Overall stats of the round so far
    print(f"***Round Update***")
    print(f"{result}")
    print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

# Show round result
if user_points < computer_points:
    print("You have lost this round meaning no points "
          "have been added to your total score. The computer's score has "
          f"increased by {computer_points} points. ")
else:
    print(f"Good job! You have won the round and {user_points} points have "
          f"been added to your score")

