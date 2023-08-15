a = "aeroplane ssscAAABM345"

b = a.startswith("a")  # print  true or false if argument present in 1st position
print(b)

b = a.endswith("45")  # print  true or false if argument present in last position
print(b)

b = a.isalpha()  # print true or false if char present in string
print(b)

b = a.isdigit()  # print true or false if number present in string
print(b)

b = a.isalnum()  # print true or false if number and char present in string
print(b)

a = "  \n\t"  # print true or false if only space present in string
b = a.isspace()
print(b)

a = "Abh Wogb"
b = a.istitle()
print(b)
