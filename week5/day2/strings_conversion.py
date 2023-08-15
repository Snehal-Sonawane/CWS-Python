a = "snehal is student"
print(list(a))

a = ["snehal", "wer", "abc"]
b = " ".join(i for i in a)
print(b)

a = [34, 56, 78]
b = " ".join(str(i) for i in a)
print(b)

a = [34, 56, 78]
b = "-".join(str(i) for i in a)
print(b)

a = [34, 56, 78]
b = " | ".join(str(i) for i in a)
print(b, type(b))

a = [34, 56, 78]
b = " ".join(str(i + 4) for i in a)
print(b)
