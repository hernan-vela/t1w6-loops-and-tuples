numbers = [3, 41, 12, 9, 74, 15]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("The largest number is", largest)