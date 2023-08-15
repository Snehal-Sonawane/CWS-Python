a = [11, 22, 34, 67, 23]

for i in range(0, len(a)):  # via position
    print(a[i])

for i in a:  # via value
    print(i)

for i in a:  # iteration by value
    if i % 2 == 0:
        print(i)

total = 0
for i in a:
    total = total + i
print(total)


a = []
for i in range(0, 5):
    num = int(input("Enter an integer: "))
    a.append(num)
print(a)
