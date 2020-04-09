"""Binary Search

You'll need a SORTED array and an item to perform a binary search

Binary Search (when sorted) has a Big O of *O(log n)*

"""


def binary_search(lst, item):
    # low and high keep track of which part of the list
    # you'll search in
    low = 0
    high = len(lst) - 1

    # while you haven't narrowed it down to one element
    # check the middle element
    while low <= high:  # While you haven't narrowed it down to one element
        mid = (low + high) // 2  # check the middle element
        print("Middle index!", mid)
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# big_list = [i+1 for i in range(128)]
big_list = [i+1 for i in range(256)]
# huge_list = [i+1 for i in range(1000000000)]

# print(big_list)
# print("My number is at index:", binary_search(example_list, 5))
# print("My number is at index:", binary_search(example_list, 23))
# print("My number is at index:", binary_search(big_list, 256))
# print("My number is at index:", binary_search(big_list, 54938))

