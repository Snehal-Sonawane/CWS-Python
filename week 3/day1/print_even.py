a = [34, 66, 22, 79, 75, 27, 16, 40]
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        print(a[i])


a = [34, 66, 22, 79, 75, 27, 16, 40]
for i in range(0, len(a)):
    if a[i] % 3 == 0 or a[i] % 4 == 0:
        print(a[i])

# print even number and sum of all even number
a = [34, 66, 22, 79, 75, 27, 16, 40]
sum = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        print(a[i])
        sum = sum + a[i]
print(sum)


# print odd number and sum of all odd number
a = [34, 66, 22, 79, 75, 27, 16, 40]
sum = 0
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        print(a[i])
        sum = sum + a[i]
print(sum)


# sum of all elements in list then till if list is even or odd
a = [34, 66, 22, 79, 75, 27, 16, 40]
sum = 0
for i in range(0, len(a)):
    sum = sum + a[i]
print(sum)
if sum % 2 == 0:
    print("list is even ")
else:
    print("list is odd")

# Q2. Make a list. Tell if the length of that list is Even or Odd.
a = [34, 66, 22, 79, 75, 27, 16, 40]
count = 0
for i in range(0, len(a)):
    count = count + 1
print(count)
if count % 2 == 0:
    print("Lengh of list is Even")
else:
    print("Length of list is Odd")
#

# reversed order
a = [34, 66, 22, 79, 75, 27, 16, 40]
print(a[::-1])


a = [34, 66, 22, 79, 75, 27, 16, 40]
for i in range(len(a), 34, -1):
    print(a[i], end=" ")


a = [1, 2, 3, 4, 5]
for i in range(5, 0, -1):
    print(i)
