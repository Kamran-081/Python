s = input().split()
longest = ""

for word in s:
    if len(word) > len(longest):
        longest = word

print(longest)
