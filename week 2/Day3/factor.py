# ask number and print factor of number
end = int(input("Enter end number = "))
for i in range(1, end + 1):
    if end % i == 0:
        print(i, end=" ")


# ask number and print factor of number and count factor
end = int(input("Enter end number = "))
count = 0
for i in range(1, end + 1):
    if end % i == 0:
        count = count + 1
        print(f"factor is {i} ")
print(f"count is {count}")
