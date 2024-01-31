# Checks that the user has entered an integer
while True:

    error = "Please choose an integer that is 13 or greater"

    # Checks that a number is higher or equal to 13
    try:
        my_num = int(input("Enter an Integer: "))
        if my_num < 13:
            print(error)
        else:
            print("Your number is ", my_num)

    except ValueError:
        print(error)
