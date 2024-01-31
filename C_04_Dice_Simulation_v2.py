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
    print(roll_1)
    roll_2 = roll_die()
    print(roll_2)
    # Checks if it's possible to double the score

    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points after the first dice roll
    user_points = roll_1 + roll_2

    # Shows the result of the dice rolls
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")
    print(f"Double score opportunity: {double_score}")
    return user_points, double_score


# Main routine goes here
how_many = int(input("How many dice? (1 or 2): "))

for item in range(0, 5):
    if how_many == 2:
        start_points = double_roll()
        points = start_points[0]
        double_points = start_points[1]

        print(f"You have {points} points and a double score of {double_points}")
