import random


def roll_die():
    result = random.randint(1, 6)
    return result


# Main routine goes here
for item in range(0, 5):
    user_score = 0
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
    print(f"Die 1: {roll_1} \t Die 2: {roll_2} \t Points: {user_points}")
    print(f"Double score opportunity: {double_score}")
