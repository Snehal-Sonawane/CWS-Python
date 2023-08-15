# append
a = [1, 3, 4, 46]
print(a)
a.append(100)
a.append(50)  # add 100 end of the list
print(a)

a = []
a.append(100)
a.append(50)
print(a)


# insert
a = [1, 3, 4, 46]
a.insert(2, 34)  # 2 is position 34 value
print(a)
a.insert(-1, 100)
print(a)
a.insert(500, 55)  # in this case no 500 position then insert in last
print(a)

# pop
a = [1, 3, 4, 46, 55, 66, 77, 89]
a.pop()  # remove last element
print(a)

a = [1, 3, 4, 46, 55, 66, 77, 89]
a.pop()
a.pop()
a.pop()
print(a)

a = [1, 3, 4, 46, 56, 77, 89]
a.pop(2)  # 2 is position
print(a)

# remove
a = [1, 3, 4, 46, 56, 77, 4, 89]
a.remove(3)  # 3 is value
print(a)

a = [1, 3, 4, 46, 56, 77, 4, 89]
a.remove(4)  # in this case remove only 1st one value of 4
print(a)
