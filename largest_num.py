
integers_list = [ 15, 766, 19, 2, 4, 5, 70, 99, 1, 722]

largest = integers_list[0]

for i in integers_list:
    if i > largest:
        largest = i

print(f"The largest number of the given list of integers is {largest}")