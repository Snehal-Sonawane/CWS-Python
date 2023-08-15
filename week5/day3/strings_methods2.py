a = "   xyz@gmail.com   "

b = a.strip()  # strip() first and last space trim
print(b)

a = "   xyz@gmail.com@"
b = a.strip("@")  # strip("@") means last @ get trim
print(b)


b = a.lstrip()  # left side space trim
print(b)

b = a.rstrip()  # right side space trim
print(b)

b = a.count("g")  # count number of g present in string
print(b)

a = "   xyz@gmail.com@"
b = a.find("g")  # gives position
print(b)

a = "   xyz@gmail.com@"
b = a.index("g")  # gives position
print(b)
