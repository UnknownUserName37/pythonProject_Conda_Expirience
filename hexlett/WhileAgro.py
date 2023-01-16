def join_numbers_from_range(num_1, num_2):
    text = ''
    i = num_1

    while i <= num_2:
        text += str(i)
        i += 1
        print(i)
    return text


print(join_numbers_from_range(4, 7))
