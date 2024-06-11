# # Initialising a variable
# string_list = ["Coder", "Academy", "Champion"]
# result = 0


# for string in string_list:
#     for letter in string:
#         if letter in "Cc":
#             result += 1
# print("The total occurence of C in the list: ", result)

# 1. Define or establish variable and set up the starting point (count, result, total, etc)
colours = ["marble", "ivory", "scarlett", "crimson", "mauve"]
count = 0

# 2. Establish condition for the loop
for word in colours:
    for letter in word:
        if letter in "Rr":
            count += 1

# 3. Tell the program what to return as after the process            
print("The number of letters r among all the entries of the list colour is", count)
print(f"The number of letters R among all the entries of the list colours is {count}")