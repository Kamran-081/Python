t = (10, 20, 30, 20, 40, 50)

print("Tuple:", t)

print("Length:", len(t))

print("Max:", max(t))

print("Min:", min(t))

print("Sum:", sum(t))

print("Count of 20:", t.count(20))

print("Index of 30:", t.index(30))

t2 = tuple([60, 70, 80])
print("New Tuple from list:", t2)

t3 = t + t2
print("Concatenation:", t3)

print("Slicing:", t3[1:5])

print("Membership:", 40 in t3)
