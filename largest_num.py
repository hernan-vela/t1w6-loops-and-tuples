
# integers_list = [ 15, 766, 19, 2, 4, 5, 70, 99, 1, 722]

# largest = integers_list[0]

# for i in integers_list:
#     if i > largest:
#         largest = i

# print(f"The largest number of the given list of integers is {largest}")


# Nancho exercise:
# Cooper Test, maximum number of rounds in race track in 12 min
# Rounds of 10 runners in 12 mins are supplied below:

runners_times = [9, 9.5, 12, 10, 10, 11, 5, 9, 9.5, 11.5]
highest_score = runners_times[0]

for time in runners_times:
    if time > highest_score:
        highest_score = time #in Python the of variables matters
print(f"The runner with the highest number of rounds made {highest_score} laps")

