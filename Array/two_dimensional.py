import numpy as np

# Record of temperatures 4 times a day

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

two_dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(two_dimensional_array)
print(two_dimensional_array.ndim)
print(two_dimensional_array.shape)

# Insertion
# 1. Adding column

new_two_dimensional_array = np.insert(
    two_dimensional_array,
    0, # at what position you want to add
    [[1,2,3,4]], # the column or row
    axis=1 # 0 -> row, 1 -> column
)

print(new_two_dimensional_array)

# 2. Adding row

new_two_dimensional_array = np.insert(
    two_dimensional_array,
    0,
    [[1,2,3,4]],
    axis=0
)

print(new_two_dimensional_array)
print(new_two_dimensional_array.ndim)
print(new_two_dimensional_array.shape)

new_two_dimensional_array = np.append(
    two_dimensional_array,
    [[1,2,3,4]],
    axis=0
)

print(new_two_dimensional_array)

# Accessing

def access_elements(array, rowIndex, columnIndex):
    try:
        return array[rowIndex][columnIndex]
    except IndexError:
        # raise IndexError("Index out of range")
        print("Index out of range")

def traverse_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=" ")
        print()

if __name__ == '__main__':
    print(access_elements(two_dimensional_array, 10, 1))
    print(len(new_two_dimensional_array))
    print(traverse_array(new_two_dimensional_array))

    new_two_dimensional_array = np.delete(two_dimensional_array, 0, axis=0) # axis 0 -> row, axis 1 -> col
