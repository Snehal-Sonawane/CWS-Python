# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
n = 5
p = 1
for i in range(n):
    for j in range(i + 1):
        print(p, end=" ")
    p = p + 1
    print()


#   1 1 1 1 1
#     2 2 2 2
#       3 3 3
#         4 4
#           5
n = 5
p = 1
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n):
        print(p, end=" ")
    p = p + 1
    print()


#           1
#         2 2 2
#       3 3 3 3 3
#     4 4 4 4 4 4 4
#   5 5 5 5 5 5 5 5 5
n = 5
p = 1
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print(p, end=" ")
    for j in range(i + 1):
        print(p, end=" ")
    p = p + 1
    print()


#  1  1  1  1  1  1  1
#     2 2 2 2 2 2 2
#       3 3 3 3 3
#         4 4 4
#           5
n = 5
p = 1
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n - 1):
        print(p, end=" ")
    for j in range(i, n):
        print(p, end=" ")
    p = p + 1
    print()


# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1
n = 5
p = 5
for i in range(n):
    for j in range(i + 1):
        print(p, end=" ")
    p = p - 1
    print()


#           1
#         1 2 3
#       1 2 3 4 5
#     1 2 3 4 5 6 7
#   1 2 3 4 5 6 7 8 9
n = 5
for i in range(n):
    p = 1
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print(p, end=" ")
        p = p + 1
    for j in range(i + 1):
        print(p, end=" ")
        p = p + 1
    print()


#   5 5 5 5 5
#     4 4 4 4
#       3 3 3
#         2 2
#           1

n = 5
p = 5
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n):
        print(p, end=" ")
    p = p - 1
    print()


#           5
#         4 4 4
#       3 3 3 3 3
#     2 2 2 2 2 2 2
#   1 1 1 1 1 1 1 1 1
n = 5
p = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print(p, end=" ")
    for j in range(i + 1):
        print(p, end=" ")
    p = p - 1
    print()


#   5 5 5 5 5 5 5 5 5
#     4 4 4 4 4 4 4
#       3 3 3 3 3
#         2 2 2
#           1
n = 5
p = 5
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n - 1):
        print(p, end=" ")
    for j in range(i, n):
        print(p, end=" ")
    p = p - 1
    print()

# 1
# 2 2
# 1 1 1
# 2 2 2 2
# 1 1 1 1 1
n = 5
for i in range(n):
    for j in range(i + 1):
        if i % 2 == 0:
            print("1", end=" ")
        else:
            print("2", end=" ")

    print()


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
n = 5
for i in range(n):
    p = 1
    for j in range(i, n):
        print(p, end=" ")
        p = p + 1
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n = 5
for i in range(n):
    p = 1
    for j in range(i + 1):
        print(p, end=" ")
        p = p + 1
    print()


# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
n = 5
for i in range(n):
    p = 5
    for j in range(i + 1):
        print(p, end=" ")
        p = p - 1
    print()
