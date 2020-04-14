"""Quick Sort

Some good examples include the farming land plot. We want to split them up into EVEN, SQUARE plots that are all the same. We can split them into big even squares, but we have
and odd rectangle left over. So, recursion comes handy, and we split that into even plots until we get to an uneven rectangle. Go again until you cannot, that's your base case
Then, you will see that for a 1680 x 640 plot of land, if you have EVEN, SQUARE plots all throughout, you have 80 x 80 as your largest plot.

"""

"""Quicksort

Below is Actual Quicksort

Steps:
1. Pick a pivot.
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot
3. Call quicksort recursively on the two sub-arrays

"""




import random
def quicksort(arr):
    if len(arr) < 2:  # if it is an empty array or if it has one item
        return arr  # Base case: arrays with 0 or 1 element are already "sorted"
    else:
        pivot = arr[0]  # recursive case
        # sub array of all the elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # sub array of all the elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# def quicksort2(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = random.choice(arr)
#         for i in arr[1:]:
#             if i <= pivot:


test_list = [12, 23, 34, 45, 98, 87, 76, 65, 54, 43]

print("QUICKSORT:", quicksort(test_list))
# Here is another divide and conquer strategy:

# A Function to add the sum of numbers


def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(sum([1, 2, 3, 4]))

# Now, let's think of how to do this using recursion

"""Steps to solving this using Recursion:

1. Find the base case. An array with 0 or 1 element, that would be the base case
Either [] for an empty array, 0
or [7] (arbitrary number) because the sum would just be 7
2. You need to move closer to an empty array with every recursive call.
    sum(2,4,6) = 12
    is the same as
    2 + sum(4,6) = 2 + 10 = 12


"""
# 4.1 Code

# DOES NOT WORK
# def recursive_binary(arr, target):
#     low = 0
#     high = len(arr)-1
#     if low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == target:
#             return mid
#         elif guess > target:
#             return recursive_binary(arr[low:mid], target)
#         else:
#             return recursive_binary(arr[mid:high], target)
#     return None


# test = [45, 23, 53, 23, 26, 456, 85, 345, 13]

# print(recursive_binary(test, 53))
