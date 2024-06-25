# # # Range function (start = 0, stop = n, step = 1) These are the default values if nothing is specified.

# # # # For loop in a range:
# # for i in range (2, 7, 1):
# #     print(i)
# # print("----------")
# # for i in range (2, 20, 2):
# #     print(i)
# # print ("---------")

# # # for i in range(10, 5, -2): 
# # #     print(i)
# # # for n in range(10, 20, 2):
# # #     print(n)
# # for i in range (2, 7):
# #     print(i)


# # #This range goes until "1001" to include "1000" in the output
# # for i in range (0, 1001, 200):
# #     fact_twenty = i
# #     print(f"{fact_twenty} is a factor of 20.")
          
    
# For loop in a list
fruits = ["Apple", "Banana", "Guava", "Papaya", "Cherry", "Pineapple", "Dragon fruit", "Coconut", "Mandarine"]
for i in fruits:
    print(i)

# # It prints each letter in string "CoderAcademy":
# for each in "CoderAcademy":
#     print(each)

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
