s1 = input().split()
s2 = input().split()
a = []
for x in s1:
    if x not in a:
        a.append(x)
b = []
for x in s2:
    if x not in b:
        b.append(x)
print(*a)
print(*b)
