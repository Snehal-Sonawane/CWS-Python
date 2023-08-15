# ask a number from user
# 1 to n
num = int(input("Enter start number = "))
end = int(input("Enter end number = "))
for i in range(num, end + 1):
    print(i, end=" ")


# ask a number from user
# 1 to n
num = int(input("Enter number = "))
for i in range(1, num + 1):
    print(i, end=" ")

# divisible by 8 print all those number
num = int(input("Enter end number = "))
for i in range(1, num + 1):
    if i % 8 == 0:
        print(i, end=" ")
# divisible by 8 count those number
num = int(input("Enter end number = "))
count = 0
for i in range(1, num + 1):
    if i % 8 == 0:
        count = count + 1

print(count, end=" ")


# divisible by 8 count those number and sum of all thouse number
num = int(input("Enter end number = "))
count = 0
sum = 0
for i in range(1, num + 1):
    if i % 8 == 0:
        count = count + 1
        sum = sum + i
print(count, sum, end=" ")
