a = [34, 56, 11, 22, 55]
b = list(a)
print(b, type(b))
b.append(200)
print(b)
a = tuple(b)
print(a)
