from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    """
    Set up the context and prepare the call to the specified
    algorithm using the supplied array. Only import the
    algorithm function if it's not the built-in `sorted()`  
    """
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        # Loop throgh array until poition n-i-1
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                # Swap Elements
                array[j], array[j+1] = array[j+1], array[j]
                already_sorted = False

        if already_sorted:
            break
    return array
            
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i-1

        while j>=0 and array[j] > key_item:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = array[j]
    return array

def merge(left, right):
    if len(left) == 0:
        # left array is empty nothing has to be merged
        return right
    if len(right) == 0:
        # right array is empty nothing has to be merged
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        
        # If end of an array is reached append other array to result
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    if len(array) < 2:
        return array
    
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


ARRAY_LENGTH = 10_000

if __name__ == "__main__":
    # Genareate an Array of ARRAY_LENGTH items consisting of
    # random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array just created
    run_sorting_algorithm(algorithm="merge_sort", array=array)