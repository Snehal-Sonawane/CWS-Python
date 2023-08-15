a = "areoplane is bid trasport"
count = 0
for i in a:
    if i == "o":
        count = count + 1
print(count)

a = "areoplane is big trasport"
count = 0
for i in a:
    if i == "o" or i == "O":
        count = count + 1
print(count)

# in sentance user letter present or not if present then print yes
sen = input("Enter a sen = ")
let = input("Enter a letter = ")
count = 0
for i in sen:
    if i == let:
        count = count + 1
# print(count)
if count > 0:
    print("yes")
else:
    print("no")

# 2nd method
a = input("Enter an sentence: ")
b = input("enter a letter = ")

if b in a:
    print("yes")
else:
    print("no")
