a = [34, "snehal", 66.5, 0, 2, 18, 24]
for i in range(0, len(a)):
    print(a[i])


# even number
a = [34, 66.5, 2, 18, 24]
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        print(a[i])

# sum od all even number
a = [34, 66.5, 2, 18, 24]
sum = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        sum = sum + a[i]
print(sum)

# revered
a = [34, 66, 2, 18, 24]
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")
# revered
a = [34, 66, 2, 18, 24]
for i in range(4, -1, -1):
    print(a[i], end=" ")
