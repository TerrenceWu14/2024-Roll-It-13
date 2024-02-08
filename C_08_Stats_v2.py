# Finds the lowest, highest and the average score from a list
def get_stats(stats_list):
    # Sorts the lists
    stats_list.sort()
    print(f"{user_scores}")
    print(f"{computer_scores}")
    # Finds the lowest, highest and the averages
    lowest_score = user_scores[0]
    highest_score = user_scores[-1]
    average_score = sum(user_scores) / len(user_scores)
    return [lowest_score, highest_score, average_score]


# Create lists to hold the user and computer scores
user_scores = [10, 0, 13, 7, 10, 11]
computer_scores = [10, 11, 0, 0, 10, 11]
# Loop six times - for testing purposes,
# asks the user to enter the scores for each round
# for i in range(0, 6):
# user_score = int(input("Enter the user score: "))
# computer_score = int(input("Enter the computer score: "))
#
# # Adds user score to list of user scores
# user_scores.append(user_score)
# computer_scores.append(computer_score)
# # Calculate the lowest, highest and average scores
# # and display them
#
# # Sorts the lists
# user_scores.sort()
# computer_scores.sort()
#
# print(f"{user_scores}")
# print(f"{computer_scores}")
#
# user_low = user_scores[0]
# user_high = user_scores[-1]
# user_average = sum(user_scores) / len(user_scores)
#
# print(f"{user_low}")
# print(f"{user_high}")
# print(f"{user_average}")
user_stats = get_stats(user_scores)
print(f"Low: {user_stats[0]}")
print(f"High: {user_stats[1]}")
print(f"Average: {user_stats[2]}")
