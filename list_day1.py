                                                 # LIST IN PYTHON

# ? List can contain duplicate items.
# ? List in Python are Mutable. Hence, we can modify, replace or delete the items.
# ? List are ordered. It maintain the order of elements based on how they are added.
# ? Accessing items in List can be done directly using their position (index), starting from 0.

# Creating a List
a = [1,'hello',True,'a',['2',34]]  # Using Square Brackets

print("Here's the list a : ", a)
b = list((1,'hello',True,'a',['2',34]))  # Using list() Constructor

print("Here's the list b : ", b)

# Creating List with Repeated Elements

repeated_list = ['str'] * 5

print("Repeated List : ", repeated_list)

# Accessing List Elements

print("First element of list a : ", a[0])
print("Last element of list a : ", a[-1])

# ! Note: Lists Store References, Not Values

# ? Each element in a list is not stored directly inside the list structure. Instead, the list stores references (pointers) to the actual objects in memory. Example (from the image representation). 

# ? The list a itself is a container with references (addresses) to the actual values.
# ? Python internally creates separate objects for 1, 'hello', ['2',34] and True, then stores their memory addresses inside a.
# ? This means that modifying an element doesn’t affect other elements but can affect the referenced object if it is mutable


# Adding Elements into List

# * append(): Adds an element at the end of the list.
# * extend(): Adds multiple elements to the end of the list.
# * insert(): Adds an element at a specific position.

a = []
a.append(1)
print("List after appending 1 : ", a)

a.insert(0,2)
print("List after inserting 2 at 0th position : ", a)

a.extend([3,4,5])
print("List after extending with [3,4,5] : ", a)

# Updating Elements into List

a[1] = 10
print("List after updating 1st element to 10 : ", a)

# Removing Elements from List

# * remove(): Removes the first occurrence of an element.
# * pop(): Removes the element at a specific index or the last element if no index is specified, and returns it.
# * del statement: Deletes an element at a specified index without returning it.

a = [10, 20, 30, 40, 50]
a.remove(20)
print("List after removing 20 : ", a) # ? Remove the first occurrence of 20

a.pop(2)
print("List after removing element at 2nd index : ", a) # ? Remove the element at 2nd index

del a[0]
print("List after deleting element at 0th index : ", a) # ? Delete the element at 0th index

# Iterating Over Lists

a = [10, 20, 30, 40, 50]
for i in a:
    print(i)
    
# Here, i and val reprsents index and value respectively
for i, val in enumerate(a):
    print (i, val)
    
n = len(a)                    # ? Length of List

for i in range(n):            # ? Using range() function
    print(a[i])
    
while i < n:                 # ? Using while loop
    print(a[i])
    i += 1          
    
# On each iteration val is passed to print function
# And printed in the console.
[print(val) for val in a]     # ! Note: This method is not a recommended way to iterate through lists as it creates a new list (extra space).

# Nested Lists in Python

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix : ", matrix[1][2])