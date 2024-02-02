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

    print("Round heading goes here")
    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")
