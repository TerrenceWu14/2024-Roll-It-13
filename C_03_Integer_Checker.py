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


# Main routine goes here
target_score = num_check()
print(target_score)
