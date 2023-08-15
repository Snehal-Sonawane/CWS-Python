# update element
a = [44, 56, 89, 10, 11]
print(a)
a[0] = 100
print(a)
a[-1] = 13
print(a)

# add a number in element of list
a = [44, 56, 89, 10, 11]
a[0] = a[0] + 5
print(a)

a = [44, 56, 89, 10, 11]
a[0] = a[0] + 5
a[1] = a[1] + 5
a[2] = a[2] + 5
a[3] = a[3] + 5
print(a)

a = [44, 56, 89, 10, 11, 12, 5, 9]
for i in range(0, len(a)):
    a[i] = a[i] + 5
print(a)

# add 5 in even number and odd minus 5
a = [44, 56, 89, 10, 11, 12, 5, 9]
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        a[i] = a[i] + 5
    else:
        a[i] = a[i] - 5
print(a)

# even number 0 odd number no change
a = [44, 56, 89, 10, 11, 12, 5, 9]
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        a[i] = 0
print(a)
