import numpy as np
from tabulate import tabulate


def get_number() -> str:
    """
    Asks user for an input and strips from whitespaces.
    """
    user_input = input("Please enter a positive odd number: ").strip()
    return user_input


def validity_check() -> int:
    """
    Checks for validity of user input and transforms the string to integer.
    """
    while True:
        user_input = get_number()
        try:
            int_user_input = int(user_input)
            if int_user_input % 2 == 1 and int_user_input > 0:
                break
            else:
                print("The number must be positive and odd.")
        except ValueError:
            print("Please enter a valid number.")

    return int_user_input


def helper_list_of_lists(n: int):
    """
    Builds a helper list of lists with first entry of magic square.
    Parameter: a positive odd integer.
    Returns: list of lists
    eg. for n= 3 it returns:
                    [['!', '!', '!', '#'],
                     [ 0 ,  1 ,  0 , '!'],
                     [ 0 ,  0 ,  0 , '!'],
                     [ 0 ,  0 ,  0 , '!']]
    """
    array_of_zeros = np.zeros((n, n), dtype=int)
    list_to_transform = array_of_zeros.tolist()
    for row in list_to_transform:
        row.append("!")
    list_to_transform.insert(0, ["!"] * n + ["#"])
    list_to_transform[1][n // 2] = 1

    return list_to_transform


def magic_square(the_list, n: int):
    """
    Takes the list of lists and transforms to magic square
    with a given number of rows and columns.
    """
    # Initializing by index of 1 in the list
    i = 1
    j = n // 2
    for number in range(2, n**2 + 1):
        if the_list[i - 1][j + 1] == "!" and i - 1 == 0:
            the_list[n][j + 1] = number
            i = n
            j = j + 1
        elif the_list[i - 1][j + 1] == "!" and j + 1 == n:
            the_list[i - 1][0] = number
            i = i - 1
            j = 0
        elif the_list[i - 1][j + 1] == 0:
            the_list[i - 1][j + 1] = number
            i = i - 1
            j = j + 1
        elif the_list[i - 1][j + 1] != 0 or the_list[i - 1][j + 1] == "#":
            the_list[i + 1][j] = number
            i = i + 1
            j = j
    the_list = [sublist[:-1] for sublist in the_list[1:]]
    return the_list


# =========Main program=======

n = validity_check()
list_to_transform = helper_list_of_lists(n)
magic = magic_square(list_to_transform, n)
print(tabulate(magic))
