# for
# 0 to 10

for i in range(10):
    print(i, end=" ")

for i in range(2, 11):
    print(i, end=" ")

# start,end,step
for i in range(1, 11, 2):
    print(i, end=" ")

# start end 1-45
start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
for i in range(start, end + 1):
    print(i, end=" ")

# 10 to 1
for i in range(10, 0, -1):  # -1 means reverse
    print(i, end=" ")

for i in range(10, -10, -1):  # -1 means reverse
    print(i, end=" ")
