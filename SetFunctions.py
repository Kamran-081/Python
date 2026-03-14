s = {10, 20, 30, 40}

print("Set:", s)

s.add(50)
print("add:", s)

s.update([60, 70])
print("update:", s)

s.remove(20)
print("remove:", s)

s.discard(100)
print("discard:", s)

x = s.pop()
print("pop:", x, s)

a = {1, 2, 3}
b = {3, 4, 5}

print("union:", a.union(b))

print("intersection:", a.intersection(b))

print("difference:", a.difference(b))

print("symmetric difference:", a.symmetric_difference(b))

print("subset:", a.issubset(b))

print("superset:", a.issuperset(b))

c = a.copy()
print("copy:", c)

a.clear()
print("clear:", a)
