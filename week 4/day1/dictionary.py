# Dictionary (key:value)
# position index not allowed

a = {"name": "snehal", "age": 24, "gender": "male"}
print(a, type(a))

# how to access?
a = {"name": "snehal", "age": 24, "gender": "male", 5: 9, "adult": True}
# print(a["name"])
# print(a["age"])
# print(a["gender"])
# print(a["abx"])
print(a[5])
