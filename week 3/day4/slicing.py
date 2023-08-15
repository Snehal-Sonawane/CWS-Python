a = [34, 45, 65, 77, 22, 345, 19, 35, 66, 31]
# b=a[0:4]
# print(b)

# print(a[4:len(a)])
# print(a[-1:-6:-1])
# print(a[4:6])
# print(a[-1::-1])
# print(a[0:1])
# print(a[0:10:3])
# print(a[3:]) #nothing means to the end
# print(a[0:])
# print(a[2:-1])
# print(a[2::-1])
# print(a[6:-1])
# print(a[::-1])

# using iteration

a = [34, 45, 65, 77, 22, 345, 19, 35, 66, 31]
for i in a[3:7]:
    print(i, end=" ")

#sum
a = [34, 45, 65, 77, 22, 345, 19, 35, 66, 31]
b=sum(a[2:5])
print(b)

#length
a = [34, 45, 65, 77, 22, 345, 19, 35, 66, 31]
b=len(a[2:5])
print(b)

