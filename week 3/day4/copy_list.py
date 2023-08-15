a = [11, 22, 34, 56, 78, 90]
b = a
print(b)

a[3] = 1000
print(a)
print(b)

# change a list but b list as it is print using copy method
a = [11, 22, 34, 56, 78, 90]
b = a.copy()
a[3] = 1000
print(a)
print(b)
