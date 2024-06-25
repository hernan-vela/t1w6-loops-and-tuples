# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[0][1])
# print(matrix[1][1])
# print(matrix[2][1])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])

for rows in matrix:
    for item in rows:
        if item == rows[1]:
            print(item, end=" ")
    print()

# reps_training = [
#     [3, 4, 3, 4],
#     [4, 4, 5, 5],
#     [3, 4, 3, 3],
#     [1, 2, 2, 1]
# ]

# print(reps_training[3][2])