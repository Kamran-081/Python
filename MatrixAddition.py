r, c = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(r)]
b = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    for j in range(c):
        print(a[i][j] + b[i][j], end=" ")
    print()
