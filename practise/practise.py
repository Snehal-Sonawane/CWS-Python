# 2nd
num = int(input("Enter number = "))
sum = 0
for i in range(1, num + 1):
    sum = sum + i
print(sum)

# 4th
num = int(input("Enter the number= "))
total_prime = 0
for number in range(1, num + 1):
    factors = 0
    for j in range(1, number + 1):
        if number % j == 0:
            factors = factors + 1
    if factors == 2:
        total_prime += 1
print(f"Total prime = {total_prime}")

# 1st
num = int(input("Enter number = "))
square_root = num**0.5
if num % square_root == 0:
    print("It is square root")
else:
    print("It is not square root")

# 3rd
num = int(input("Enter number = "))
while num > 0:
    print(num % 10, end=" ")
    num = num // 10

# 5th
a = [23, 66, 90, 43, 98, 1]
max = 0
for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
print(max)

# 6th
a = [23, 66, 90, 43, 98, 1]
sum = 0
for i in range(0, len(a)):
    sum = sum + a[i]
print("Addition = ", sum)
avg = sum / len(a)
print("Average = ", avg)
