# Guessing Game

prize_num = 14

user_guess = None

while user_guess != prize_num:
    user_guess = int(input("Enter a number between 1 and 20 win the prize: "))
    if user_guess > prize_num:
        print("You are over. Dial down")
    elif user_guess < prize_num:
        print("Don't be timid. Go higher!")
    else:
        print("Winner, winner, chicken dinner!")







# guess_num = 5

# user_guess = None

# # while user_guess != guess_num:
# #     user_guess = int(input("What's your guess (between 1 and 10)? "))

# # print("Correct!")

# #Make it better
# #Give hints

# while user_guess != guess_num:
#     user_guess = int(input("What's your guess (between 1 and 10)? "))

#     if user_guess < guess_num:
#         print("Too low!")
#     elif user_guess > guess_num:
#         print("Too high!")
#     else:
#         print("Correct!")

