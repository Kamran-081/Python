d = {"a": 3, "b": 1, "c": 2}

sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))

print(sorted_d)
