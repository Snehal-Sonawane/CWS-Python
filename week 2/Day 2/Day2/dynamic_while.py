# enter start number =45
# enter end number = 10

# print 45 44 43......10

start = int(input("Enter start number="))
end = int(input("Enter end number = "))
i = start
while i >= end:
    print(i, end=" ")
    i = i - 1
