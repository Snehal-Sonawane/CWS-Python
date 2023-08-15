# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# incresing triangle
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()


# decresing triangle
n = 5
for i in range(5):
    for j in range(i, n):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(i, 5):
        print("*", end=" ")
    print()


# decresing+incresing triangle
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
for i in range(5):
    for j in range(i, 5):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()


# incresing and decresing triangle
#  * * * * *
#     * * * *
#       * * *
#         * *
#           *
for i in range(5):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, 5):
        print("*", end=" ")
    print()

# hill pattern
#           * *
#         * * * *
#       * * * * * *
#     * * * * * * * *
#   * * * * * * * * * *
for i in range(5):
    for j in range(i, 5):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    for i in range(i + 1):
        print("*", end=" ")
    print()

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
for i in range(5):
    for j in range(i, 5):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for i in range(i + 1):
        print("*", end=" ")
    print()


# incresing+decresing+decresing triangle
#  * * * * * * * * * *
#     * * * * * * * *
#       * * * * * *
#         * * * *
#           * *
for i in range(5):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, 5):
        print("*", end=" ")
    for j in range(i, 5):
        print("*", end=" ")
    print()


#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *
for i in range(5):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, 5 - 1):  # 5-1 means n-1 and n is 5
        print("*", end=" ")
    for j in range(i, 5):
        print("*", end=" ")
    print()


# diamond pattern
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *
for i in range(5):
    for j in range(i, 5):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(5):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, 5 - 1):
        print("*", end=" ")
    for j in range(i, 5):
        print("*", end=" ")
    print()


#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *

for i in range(5 - 1):  # 5-1 means n-1 to delete one row
    for j in range(i, 5):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(5):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, 5 - 1):
        print("*", end=" ")
    for j in range(i, 5):
        print("*", end=" ")
    print()
