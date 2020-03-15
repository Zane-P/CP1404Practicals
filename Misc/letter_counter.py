import string


def count_letters(input_str):
    counter = 0
    for char in input_str:
        if char.lower() in string.ascii_lowercase:
            counter += 1
    return counter


print(count_letters("Test123"))
