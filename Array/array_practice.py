from array import array

# 1. Create an array and traverse
my_array = array('i', [1,2,3,4,5,6])

print('Soln 1')
for i in my_array: # Space complexity of Traversing is O(n)
    print(i)

# 2. Access individual elements through indexes

print('Soln 2')
print(my_array[3])

# 3. Append any value to the array using append() method

print('Soln 3')
my_array.append(7)
print(my_array)

# 4. Insert value in an array using insert() method

print('Soln 4')
my_array.insert(2, 9)
print(my_array)

# 5. Extend python array using extend() method

print('Soln 5')
my_array2 = array('i', [22, 34, 90])
my_array.extend(my_array2)
print(my_array)

# 6. Add items from list into array using fromlist() method

print('Soln 6')
templist = [20, 21, 22]
my_array.fromlist(templist) # fromlist accepts a list only to extend
print(my_array)

# 7. Remove any array element using remove() method

print('Soln 7')
my_array.remove(22) # removes the first occurrence of the element from the list
print(my_array)

# 8. Remove last array element using pop() method

print('Soln 8')
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using index() method

print('Soln 9')
print(my_array.index(21))

# 10. Reverse a python array using reverse() method

print('Soln 10')
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method

print('Soln 11')
print(my_array.buffer_info()) # (1818923555760 -> address, 12 -> length of the array)

# 12. check for number of occurrence of an element using count() method

print('Soln 12')
print(my_array.count(21))

# 13. Convert array to python list using tolist() method

print('Soln 13')
print(my_array.tolist())

# 14. Slice elements from a list

print('Soln 14')
print(my_array[1:4])
print(my_array[1:4:2])
print(my_array[::-1]) # reverse
