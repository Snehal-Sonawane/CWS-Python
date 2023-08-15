start = int(input("Enter start number ="))
end = int(input("Enter end number ="))
i = start
while i <= end:
    if i % 5 == 0 and i % 6 == 0:
        print(i, end=" ")
    i = i + 1

start = int(input("Enter start number ="))
end = int(input("Enter end number ="))
i = start
if start <= end:
    while i <= end:
        if i % 5 == 0 and i % 6 == 0:
            print(i, end=" ")
        i = i + 1
else:
    print("start is greater")


start = int(input("Enter start number ="))
end = int(input("Enter end number ="))
i = start
if start <= end:
    while i <= end:
        if i % 5 == 0 and i % 6 == 0:
            print(i, end=" ")
        i = i + 1
else:
    while i >= end:
        if i % 5 == 0 and i % 6 == 0:
            print(i, end=" ")
        i = i - 1
