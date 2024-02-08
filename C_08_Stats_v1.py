# Create lists to hold the user and computer scores
user_scores = []
computer_scores = []
# Loop six times - for testing purposes,
# asks the user to enter the scores for each round
for i in range(0, 6):
    user_score = int(input("Enter the user score: "))
    computer_score = int(input("Enter the computer score: "))
    # Adds user score to list of user scores
    user_scores.append(user_score)
    computer_scores.append(computer_score)
# Calculate the lowest, highest and average scores
# and display them
# Sorts the lists
user_scores.sort()
computer_scores.sort()
print(f"{user_scores}")
print(f"{computer_scores}")
user_low = user_scores[0]
user_high = user_scores[-1]
user_average = sum(user_scores) / len(user_scores)
print(f"{user_low}")
print(f"{user_high}")
print(f"{user_average}")