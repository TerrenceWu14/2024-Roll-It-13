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

    # Tells the user if they are eligible for double points or if it's the computer
    if double_score == "no":
        double_message = ""
    elif double_score == "yes":
        double_message = (f"{who} is eligible to win double the points"
                          " if you win this round since you got a pair! 🙌🙌")
        print(double_message)
    # Shows the result of the dice rolls
    return first_points, double_score


# Main routine goes here
print("Press <enter> to begin this round (roll the 🎲): ")
input()
# Gets the initial points for the user
user_first = double_roll("You")
user_points = user_first[0]
user_double_points = user_first[1]

# Gets initial dice rolls for computer
computer_first = double_roll("Computer")
computer_points = computer_first[0]
computer_double_points = computer_first[1]

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
    # If user points > computer points it tells you that you're ahead or if it's a tie
    if user_points > computer_points:
        result = "🙂You are ahead🙂"
    elif computer_points > user_points:
        result = "😧The Computer is ahead😧"
    else:
        result = "😬 Its a tie 😬"
    # Overall stats of the round so far
    print(f"⁕⁕⁕Round Update⁕⁕⁕")
    print(f"{result}")
    print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

# Show round result
if user_points < computer_points:
    if computer_double_points == "yes":
        computer_points *= 2
    print("You have lost this round meaning no points "
          "have been added to your total score. The computer's score has "
          f"increased by {computer_points} points. ")

else:
    # Check if either user or computer is eligible for double points
    if user_double_points == "yes":
        user_points *= 2
    print(f"🥳🥳🥳 You have won the round and {user_points} points have "
          f"been added to your score 🥳🥳🥳")

