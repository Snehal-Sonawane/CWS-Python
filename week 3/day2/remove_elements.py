# to remove same multiple value in list
a = [43, 4, 5, 68, 77, 43]
while a.count(43) > 0:
    a.remove(43)
print(a)


# to put in value in b expect 43
a = [43, 4, 5, 68, 77, 43]
b = []
for i in range(0, len(a)):
    if a[i] != 43:
        b.append(a[i])
print(a)
print(b)
