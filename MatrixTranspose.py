r, c = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(r)]

transpose = [[0]*r for _ in range(c)]

for i in range(r):
    for j in range(c):
        transpose[j][i] = mat[i][j]

for row in transpose:
    print(*row)
  
