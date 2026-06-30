import array

my_array = array.array("i", [1, 2, 3, 4, 5])
my_array2 = array.array("d", [1, 2, 3, 4, 5, 3.5])

# import numpy as np
#
# my_array_np = np.array([], dtype=int)

# def traverse_array(arr):
#     for i in arr:
#         print(i)

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

if __name__ == "__main__":
    # print(list(my_array))
    # print(list(my_array_np))

    # my_array.insert(0, 6)
    # print(my_array)

    # traverse_array(my_array)

    # print(linear_search(my_array, 2))
    # print(linear_search(my_array, 8))

    my_array3 = my_array.remove(3)
    print(my_array)  # array('i', [1, 2, 4, 5])
    print(my_array3)  # None
