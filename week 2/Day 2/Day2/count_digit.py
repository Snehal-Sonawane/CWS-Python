# ask number from user=
# 2234
# result =4

num = int(input("Enter number = "))
count = 0
while num > 0:
    count = count + 1
    num = num // 10
print(count)
