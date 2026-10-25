a = input()
b = input()
c = input()
d = input()
x = [a, b, c, d]
m = -1
r = ""
for s in x:
    n = 0
    for i in s:
        if i.isdigit():
            n += int(i)
    if n > m:
        m = n
        r = s
print(r)
