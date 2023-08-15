# add number in end and number ask by user
a = [12, 23, 45, 66]
num = int(input("Enter an integer: "))
a.append(num)
print(a)

# insert number and position by user
a = [12, 23, 45, 66]
num = int(input("Enter an integer: "))
position = int(input("Enter an position: "))
a.insert(position, num)
print(a)

# print list in revered
a = []
len = int(input("Enter an integer: "))
for i in range(0, len):
    num = int(input("Enter an integer: "))
    a.insert(-len, num)
print(a)

# 2nd method for revered
a = []
len = int(input("Enter an integer: "))
for i in range(0, len):
    num = int(input("Enter an integer: "))
    a.insert(0, num)
print(a)


# count 55 number in list
a = [55, 56, 78, 23, 44, 22, 55, 21, 10, 55]
count = 0
for i in range(0, len(a)):
    if a[i] == 55:
        count = count + 1
print(count)

# count prime number
a = [2, 5, 6, 9, 11]
count = 0
for i in range(0, len(a)):
    factors = 0
    for j in range(1, a[i] + 1):
        if a[i] % j == 0:
            factors += 1
    if factors == 2:
        count += 1
print(count)

a = [2, 5, 10, 12, 17, 19, 4]
factor = 0
for i in range(0, len(a)):
    if a[i] % i == 0:
        factor = factor + 1
print(factor)
if factor == 2:
    print("prime")
else:
    print("composite")


num = int(input("Enter an integer: "))
factor = 0
for i in range(1, num + 1):
    if num % i == 0:
        factor = factor + 1
print(f"factor is {factor}")
if factor == 2:
    print("prime number")
else:
    print("composite number")
