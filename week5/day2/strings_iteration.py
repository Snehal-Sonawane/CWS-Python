a = "aeroplane"
print(a[0])
print(a[1])
print(a[-1])
print(a[2:5])
print(a[::-1])
print(a)
# immutable
a[0] = "z"  # not allowed because strings are immutable
print(a)
a = 5
print(a)


a = "aeroplane"
for i in range(0, len(a)):
    print(i)  # print 123

a = "aeroplane"
for i in range(0, len(a)):
    print(a[i])  # print chr

a = "aeroplane"
for i in a:
    print(i)  # print chr

# reversed
a = "aeroplane"
for i in a[::-1]:
    print(i, end="")

a = "aeroplane"
for i in range(len(a) - 1, -1, -1):
    print(a[i], end="")
