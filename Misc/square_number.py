

def square(number):
    """
    Returns the square of an input.
    :param number:
    :return:
    """
    try:
        return number * number
    except TypeError:
        print("The input is not a number.")
        return


print(square(5))