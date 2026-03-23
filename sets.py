# A set is an unordered, mutable collection of unique elements.

a = {1,3,4,5,2,1}
print(a)      #Duplicates removed automatically.

c = {1, 2, 3}
b = {3, 4}

print(c | b)   # union
print(c & b)   # intersection
print(c - b)   # difference


# Set Methods

a.add(9)
print(a)
a.remove(9)
print(a)
