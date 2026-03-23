n = int(input())
s = str(n)
power = len(s)

total = 0
for digit in s:
    total += int(digit) ** power

if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")
