for i in range(1, 4):
    print(i)
    for j in range(10, 14):
        print(j)


for i in range(1, 4):
    for j in range(10, 14):
        print(j)
    print(i)


for i in range(1, 4):
    for j in range(10, 14):
        print(i, end=" ")
        print(j, end=" ")


for i in range(1, 4):
    for j in range(10, 14):
        print(i, end=" ")


for i in range(1, 4):
    for j in range(10, 14):
        print(i, j)
