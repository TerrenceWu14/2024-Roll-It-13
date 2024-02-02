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

target_score = num_check("Enter a target score: ")
print(target_score)

while user_score < target_score and computer_score < target_score:
    print("Round heading goes here")
    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")