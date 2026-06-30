shopping_list = ["apple", "banana", "cherry"]
print(shopping_list)

for item in range(len(shopping_list)):
    shopping_list[item] += "+"

print(shopping_list) # ['apple+', 'banana+', 'cherry+']