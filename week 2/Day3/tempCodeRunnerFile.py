end = int(input("Enter end number = "))
for i in range(1, end + 1):
    if end % i == 0:
        print(i, end=" ")