l = [10, 20, 30, 40]

print("Original list:", l)

l.append(50)
print("append:", l)

l.extend([60, 70])
print("extend:", l)

l.insert(2, 25)
print("insert:", l)

l.remove(30)
print("remove:", l)

l.pop()
print("pop:", l)

l.pop(1)
print("pop with index:", l)

print("index of 40:", l.index(40))

l.append(20)
print("count of 20:", l.count(20))

l.sort()
print("sort:", l)

l.reverse()
print("reverse:", l)

l2 = l.copy()
print("copy:", l2)

l.clear()
print("clear:", l)
