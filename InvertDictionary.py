d = eval(input())

res = {}

for k, v in d.items():
    if v in res:
        if isinstance(res[v], list):
            res[v].append(k)
        else:
            res[v] = [res[v], k]
    else:
        res[v] = k

print(res)
