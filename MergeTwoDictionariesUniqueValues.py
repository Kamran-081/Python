d1 = eval(input())
d2 = eval(input())

result = {}

for k in d1:
    result[k] = d1[k]

for k in d2:
    if k in result:
        if result[k] != d2[k]:
            if isinstance(result[k], list):
                if d2[k] not in result[k]:
                    result[k].append(d2[k])
            else:
                if result[k] != d2[k]:
                    result[k] = [result[k], d2[k]]
    else:
        result[k] = d2[k]

print(result)
