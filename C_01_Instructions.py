print("🎲🎲🎲 Roll It 13 🎲🎲🎲")
print()

# Loops the code
while True:
    want_instruction = input("Do you want to read the instructions? (If so type yes or if not type no)").lower()

    # Checks whether the user entered yes or no
    if want_instruction == "yes" or want_instruction == "y":
        print("you chose yes")
    elif want_instruction == "no" or want_instruction == "n":
        print("you chose no")
    else:
        print("you didn't choose a valid option (yes/no)")
    keep_going = input("Do you want to continue?")
