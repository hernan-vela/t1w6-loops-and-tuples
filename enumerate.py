# animals = ["cat", "dog", "rabbit", "horse"]


# for index, animal in enumerate(animals):
#     print(f"{index}: {animal}")

# Using for, if, break and enumerate
fruits = ["apple", "banana", "cherry", "date"]

target = "cherry"

for index, fruit in enumerate(fruits):
    if fruit == target:
        print(f"Found '{target}' at index {index}")
        break