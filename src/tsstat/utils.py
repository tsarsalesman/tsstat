"""
Utilities
---------



"""

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return qsort(left) + [pivot] + qsort(right)

def diff(A, B):
    """Finds the difference between two given lists of ints.

    Params
    ------
    A : array_like
        An array of integers
    B : array_like
        An array of integers

    Returns
    -------
    Difference : array_like
        The difference between each associated value.
    """
    diffs = []
    for i in range(len(A)):
        diffs.append(A[i] - B[i])
    return diffs
