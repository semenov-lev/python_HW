def odd_nums(n):
    for a in range(1, n + 1, 2):
        yield print(a)


odd_to_10 = odd_nums(10)
next(odd_to_10)
next(odd_to_10)
next(odd_to_10)
next(odd_to_10)
next(odd_to_10)
next(odd_to_10)
