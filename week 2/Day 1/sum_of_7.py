num = int(input("Enter start num="))
end = int(input("Enter end number="))
i = num
sum = 0
while i <= end:
    if i % 7 == 0:
        sum = sum + i
    i = i + 1
print(sum)
