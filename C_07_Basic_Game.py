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
    if double_score == "yes":
        double_message = (f"{who} is eligible to win double the points"
                          " if you win this round since you got a pair! 🙌🙌")
        print(double_message)
    # Shows the result of the dice rolls
    return first_points, double_score


# Checks that the user has entered an integer
def num_check(question):
    error = "Please choose an integer that is 13 or greater"

    # Checks that a number is higher or equal to 13
    try:
        response = int(input(question))
        if response < 13:
            print(error)
        else:
            return response

    except ValueError:
        print(error)


# Main routine goes here

# Initialises the user score and computer score
user_score = 0
computer_score = 0

num_rounds = 0

target_score = num_check("Enter a target score: ")
print(target_score)

while user_score < target_score and computer_score < target_score:
    # Add one to the number of rounds (for the heading)
    num_rounds += 1
    print(f"Round {num_rounds}")

    # Start of a single round

    # Initialises the result and the user/computer pass
    result = ""
    user_pass = "no"
    computer_pass = "no"

    # Gets the initial points for the user
    user_first = double_roll("User")
    user_points = user_first[0]
    user_double_points = user_first[1]

    # Gets initial dice rolls for computer
    computer_first = double_roll("Computer")
    computer_points = computer_first[0]
    computer_double_points = computer_first[1]

    # While both the user and the computer have <= points it keeps looping
    while user_points < 13 and computer_points < 13:

        # If the user hasn't passed, yet then it asks if they want to roll again
        roll_again = input("Press <enter> to roll again or type any letter to pass (reminder: if you pass then you "
                           "won't roll again) ")
        # Rolls the die if the user has decided to roll again
        if roll_again == "":
            user_pass = "no"
            user_roll_again = roll_die()
            # Adds what you got from the roll onto your current points
            user_points += user_roll_again
            # Displays what you rolled and your new updated points
            print(f"You rolled a {user_roll_again}. Total points: {user_points}")
        else:
            # If the user has typed anything then it means they passed and won't roll again
            user_pass = "yes"
            print("You passed your turn")

        # Makes it so that if the user had passed before they can't roll again
        if user_pass == "yes":
            pass

        # Checks to see whether the user or computer have goner over 13 or not
        if user_points > 13:
            # Makes it so that the loser gets this rounds' points reset to 0
            user_points = 0
            break
        print()

        if 10 <= computer_points <= 13:
            computer_pass = "yes"

        elif computer_pass == "yes":
            pass

        # Rolls the die for the computer and updates its points
        else:
            computer_roll_again = roll_die()
            computer_points += computer_roll_again
            print(f"The Computer rolled a {computer_roll_again}. Total points: {computer_points}")

        if computer_points > 13:
            computer_points = 0
            break
        print()

        # If user points > computer points it tells you that you're ahead or if the computer is ahead.
        if user_points > computer_points:
            result = "🙂You are ahead🙂"
        elif computer_points > user_points:
            result = "😧The Computer is ahead😧"

        # Overall stats of the round so far
        print(f"⁕⁕⁕Round Update⁕⁕⁕")
        print(f"{result}")
        print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

        # Checks if the computer and user have both passed and whether it's a tie
        if computer_points == user_points and computer_pass and user_pass == "yes":
            result = "😬 Its a tie 😬"
            break

    # Show round result
    if user_points < computer_points:
        if computer_double_points == "yes":
            computer_points *= 2
        print("You have lost this round meaning no points "
              "have been added to your total score. The computer's score has "
              f"increased by {computer_points} points. ")
        add_points = computer_points

    elif user_points > computer_points:
        # Check if either user or computer is eligible for double points
        if user_double_points == "yes":
            user_points *= 2
        print(f"🥳🥳🥳 You have won the round and {user_points} points have "
              f"been added to your score 🥳🥳🥳")
        add_points = user_points

    elif result == "😬 Its a tie 😬":
        print(f"😔😔😔You and the computer have tied so you gain {user_points} points and the computer also gains "
              f"{computer_points} 😔😔😔.")
        add_points = user_points

    # End of a single round

    # If the user won then it adds the points to their score
    if user_points > computer_points:
        user_score += add_points
    # If the computer won then it adds the points to the computer's score
    elif computer_points > user_points:
        computer_score += add_points
    # If it's a tie then it adds the points to both the user and the computer
    else:
        user_score += add_points
        computer_score += add_points

    print()
    print(f"User Score: {user_score} | Computer Score: {computer_score}")
    print()
