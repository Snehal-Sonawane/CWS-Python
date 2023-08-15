a = [43, 4, 5, 68, 77]
print(a)
# count,index are methods always store in variable

# count
a = [43, 4, 5, 68, 77, 43]
r = a.count(43)  # to count value 43 is value in list
print(r)
print(a.count(43))

# index
r = a.index(68)  # to indentify the position of value
print(r)


# to indentify the poisition
a = [43, 4, 5, 68, 77, 43]
for i in range(0, len(a)):
    if a[i] == 43:
        print(i)
