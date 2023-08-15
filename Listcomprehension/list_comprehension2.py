a = [i for i in range(1, 100)]
print(a)

a = [i + 10 for i in range(1, 100)]
print(a)

a = [i % 2 for i in range(1, 10)]
print(a)


# print even odd
a = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(a)

a = [f"even-{i}" if i % 2 == 0 else f"odd-{i}" for i in range(1, 11)]
print(a)
print([f"even-{i}" if i % 2 == 0 else f"odd-{i}" for i in range(1, 11)])


# sum 1 to 10
print(sum([i for i in range(1, 11)]))

print(
    sum(
        [
            i
            for i in range(
                int(input("Enter start number = ")),
                int(input("Enter end number = ")) + 1,
            )
        ]
    )
)


# even number
a = [i for i in range(1, 11) if i % 2 == 0]
print(a)

a = [i + 10 for i in range(1, 11) if i % 2 == 0]
print(a)
