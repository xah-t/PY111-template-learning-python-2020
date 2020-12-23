from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    left_side = 0
    right_side = len(arr) - 1

    while left_side <= right_side:

        mid = (right_side + left_side)//2
        if arr[mid] == elem:
            return mid
        elif arr[mid] <= elem:
            left_side = mid + 1
        else:
            right_side = mid - 1
    arr = arr[left_side:right_side]
#    while arr[i] != arr[i-1]:
#        arr[i] -= 1
#    return i
    print(elem, arr)
    return None
