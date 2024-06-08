# Initialising a variable
string_list = ["Coder", "Academy", "Champion"]
result = 0


for string in string_list:
    for letter in string:
        if letter in "Cc":
            result += 1
print("The totla occurence of C in the list: ", result)
