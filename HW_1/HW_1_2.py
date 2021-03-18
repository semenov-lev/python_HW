even_cubes_array = []
sum_of_numbers_a = 0
count = 0

while count <= 999:
    count += 1
    if count % 2 != 0:
        even_cubes_array.append(count ** 3)

print(even_cubes_array)

for number in even_cubes_array:
    is_one_digits = 0 < number // 1 <= 9
    is_two_digits = 0 < number // 10 <= 9
    is_three_digits = 0 < number // 100 <= 9
    is_four_digits = 0 < number // 1000 <= 9
    is_five_digits = 0 < number // 10000 <= 9
    is_six_digits = 0 < number // 100000 <= 9
    is_seven_digits = 0 < number // 1000000 <= 9
    is_eight_digits = 0 < number // 10000000 <= 9
    is_nine_digits = 0 < number // 100000000 <= 9
    is_ten_digits = 0 < number // 1000000000 <= 9

    if is_one_digits:
        sum_of_digits = (number % 10)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_two_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_three_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_four_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_five_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_six_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_seven_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)\
                        + ((number % 10000000) // 1000000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_eight_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)\
                        + ((number % 10000000) // 1000000) + ((number % 100000000) // 10000000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_nine_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)\
                        + ((number % 10000000) // 1000000) + ((number % 100000000) // 10000000)\
                        + ((number % 1000000000) // 100000000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number
    if is_ten_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)\
                        + ((number % 10000000) // 1000000) + ((number % 100000000) // 10000000)\
                        + ((number % 1000000000) // 100000000) + ((number % 10000000000) // 1000000000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_a += number

print(sum_of_numbers_a)

sum_of_numbers_b = 0

for idx in range(len(even_cubes_array)):
    even_cubes_array[idx] += 17

for number in even_cubes_array:
    is_one_digits = 0 < number // 1 <= 9
    is_two_digits = 0 < number // 10 <= 9
    is_three_digits = 0 < number // 100 <= 9
    is_four_digits = 0 < number // 1000 <= 9
    is_five_digits = 0 < number // 10000 <= 9
    is_six_digits = 0 < number // 100000 <= 9
    is_seven_digits = 0 < number // 1000000 <= 9
    is_eight_digits = 0 < number // 10000000 <= 9
    is_nine_digits = 0 < number // 100000000 <= 9
    is_ten_digits = 0 < number // 1000000000 <= 9

    if is_one_digits:
        sum_of_digits = (number % 10)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_two_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_three_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_four_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_five_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_six_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_seven_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)\
                        + ((number % 10000000) // 1000000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_eight_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)\
                        + ((number % 10000000) // 1000000) + ((number % 100000000) // 10000000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_nine_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)\
                        + ((number % 10000000) // 1000000) + ((number % 100000000) // 10000000)\
                        + ((number % 1000000000) // 100000000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number
    if is_ten_digits:
        sum_of_digits = (number % 10) + ((number % 100) // 10) + ((number % 1000) // 100) + ((number % 10000) // 1000)\
                        + ((number % 100000) // 10000) + ((number % 1000000) // 100000)\
                        + ((number % 10000000) // 1000000) + ((number % 100000000) // 10000000)\
                        + ((number % 1000000000) // 100000000) + ((number % 10000000000) // 1000000000)
        if sum_of_digits % 7 == 0:
            sum_of_numbers_b += number

print(sum_of_numbers_b)
