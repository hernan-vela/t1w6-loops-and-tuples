# Range arguments (start = 0, stop, step = 1) - This are the default value is nothing is specified
# if you use range(10), the program will print the numbers from 0 to 9.

# print(range(5, 10, 1))

# For loop in a range
for i in range(10, 5, -2): 
    print(i)

# For loop in a list
fruits = ["Apple", "Banana", "Cherry"]

# for each in fruits:
#     print(each)

# for each in "CoderAcademy":
#     print(each)

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")