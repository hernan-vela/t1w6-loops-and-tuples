places_to_visit = ["India", "Japan", "Thailand", "Norway", "Colorado-USA", "Iceland", "New Zeland", "Germany"]

for index, place in enumerate(places_to_visit):
    print(f"{index}: {place}")


#Another example:
animals = ["cat", "dog", "rabbit", "horse"]

for index, animal in enumerate(animals):
     print(f"{index}: {animal}")

# # Using for, if, break and enumerate
# fruits = ["apple", "banana", "cherry", "date"]

# target = "cherry"

# for index, fruit in enumerate(fruits):
#     if fruit == target:
#         print(f"Found '{target}' at index {index}")
#         break

family = ["dad", "mom", "sister", "brother", "gumpling", "mother-inlaw", "sister-inlaw", "Andrew"]

for index, person in enumerate(family):
    print(f"{index}: {person}")