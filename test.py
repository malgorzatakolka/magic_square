from  magic_square import *
import numpy as np 

def test(magic_square, n: int) -> None:
    """
    Tests if the rows, columns and diagonas sums are equal to a given sum.
    The sum if calculated from formula for magic square.
    """
    ms_array = np.array(magic_square)
    sum_in_list: int = int(n * (n**2 + 1) / 2)
    equal_sums: int = 0
    diagonal_sum: int = 0

    for i in range(n):
        diagonal_sum += ms_array[i, i]
        if sum(ms_array[i]) == sum_in_list and sum(ms_array[:, i]) == sum_in_list:
            equal_sums += 1

    if equal_sums == n and diagonal_sum == sum_in_list:
        print("the function is correct")


test(magic_square, n)