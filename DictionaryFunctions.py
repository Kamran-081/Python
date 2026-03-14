d = {"a": 10, "b": 20, "c": 30}

print("Dictionary:", d)

print("Length:", len(d))

print("Value using key:", d["a"])

print("get:", d.get("b"))

print("keys:", d.keys())

print("values:", d.values())

print("items:", d.items())

d["d"] = 40
print("add element:", d)

d.update({"e": 50})
print("update:", d)

d.pop("b")
print("pop:", d)

d.popitem()
print("popitem:", d)

d2 = d.copy()
print("copy:", d2)

print("setdefault:", d.setdefault("f", 60))

d.clear()
print("clear:", d)
