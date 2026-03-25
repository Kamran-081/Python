d1 = eval(input())
d2 = eval(input())

res = {}

for k in d1:
    res[k] = d1[k]

for k in d2:
    if k in res:
        res[k] += d2[k]
    else:
        res[k] = d2[k]

print(res)
