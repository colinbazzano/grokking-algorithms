# This first is to find the smallest item in the array


def findSmallest(arr):
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


test_list = [4, 7, 2, 76, 23, 54, 9349, 29, 1, 39, 284, 29, 43, 82]


print(findSmallest(test_list))

# To then use this function and create a selection sort


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # finds the smallest element in the array, and adds it to the new array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort(test_list))
