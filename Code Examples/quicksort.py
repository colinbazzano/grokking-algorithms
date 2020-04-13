"""Quick Sort

Some good examples include the farming land plot. We want to split them up into EVEN, SQUARE plots that are all the same. We can split them into big even squares, but we have
and odd rectangle left over. So, recursion comes handy, and we split that into even plots until we get to an uneven rectangle. Go again until you cannot, that's your base case
Then, you will see that for a 1680 x 640 plot of land, if you have EVEN, SQUARE plots all throughout, you have 80 x 80 as your largest plot.

"""

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


def recursive_sum(arr):
