# Create List of Numbers with Given Range – Python

# ?  Using range()

r1 = 0
r2 = 10
li = list(range(r1,r2))
print("List of numbers with given range : ", li)

# ? Using list comprehension

li = [i for i in range(r1,r2)]
print("List of numbers with given range : ", li)

# ? Using numpy
import numpy as np
li = np.arange(r1,r2).tolist()  # arrange() works as range() in numpy and tolist() converts numpy array to list
print("List of numbers with given range : ", li)

# ? Using itertools.count()
import itertools
li = list(itertools.islice(itertools.count(r1), r2-r1)) # islice() is used to slice the iterator and count() is used to generate numbers starting from r1
print("List of numbers with given range : ", li)


# ! Ways to create a dictionary of Lists – Python

# ? Using the zip() Function

k = ['fruit', 'vegetable', 'spice']
v = ['apple', 'carrot', 'cinnamon']
di = dict(zip(k,v))
print("Dictionary of Lists : ", di)

# ? Using a Dictionary Comprehension

li = [('fruit', 'apple'), ('vegetable', 'carrot'), ('fruit', 'banana'), ('spice', 'cinnamon')]
d = {k: [i for _, i in filter(lamda x: x[0] == k, li)] for k in set(k for k,_ in li )}
print("Dictionary of Lists : ", d)

# ? Using defaultdict from collections Module

d = defaultdict(list)  # * Note: defaultdict is a subclass of the built-in dict class that returns a default value when a key is not found.
for k, v in li:
    d[k].append(v)
print("Dictionary of Lists : ", d)

# ? Using setdefault() Method

d = {}

for k, item in li:
    d.setdefault(k,[]).append(item) # * setdefault() method returns the value of the key if it is in the dictionary; otherwise, it inserts the key with the specified value.
print("Dictionary of Lists : ", d)