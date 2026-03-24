import math

a, b, c = map(float, input().split())

d = b*b - 4*a*c

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(r1, r2)
elif d == 0:
    r = -b / (2*a)
    print(r, r)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print(real, "+", imag, "i")
    print(real, "-", imag, "i")
