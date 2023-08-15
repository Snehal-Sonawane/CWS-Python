# collection of unique elements

""" position index is not allowed
   every elements will be unique """ ""
a = {12, 34, 55, 12, 12, 37, 12}  # only unique elements print
print(a)
a = {12, 34, 55, 12, 12, 37, 12, "snehal", "xyz", "xyz"}
print(a)
print(a[0])  # position index is not allowed

for i in range(0, len(a)):  # not allowed
    print(i)

a = {12, 34, 55, 12, 12, 37, 12}
for i in a:  # only iteration allowed
    print(i)
