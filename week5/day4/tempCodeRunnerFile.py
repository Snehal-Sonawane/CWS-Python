user_string = "aeroplane ok is a good mode of a transport good bye ok done"
b = user_string.split()
print(b)
for i in b:
    print(i[::-1], end=" ")