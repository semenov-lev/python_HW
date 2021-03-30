src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [
    num_2
    for num_1, num_2 in zip(src, src[1:])
    if num_2 > num_1
]

print(result)
