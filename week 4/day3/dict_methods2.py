a = {"name": "snehal", "age": 24, "gender": "male"}
a["name"] = "sonu"
print(a)

# using update
a = {"name": "snehal", "age": 24, "gender": "male"}
a.update(
    {"name": "sonu", "com": 56, "geo": 54}
)  # to update multiple key n values at a time
print(a)

# pop
a = {"name": "snehal", "age": 24, "gender": "male"}
a.pop("name")  # to delete key and value
print(a)

# ask key from user if key is exists,then delete that key
a = {"name": "snehal", "age": 24, "gender": "male"}
keyname = input("Enter keyname = ")
if a.get(keyname) != None:
    a.pop(keyname)
    print(a)
else:
    print("key does not exist")

# 2nd method
a = {"name": "snehal", "age": 24, "gender": "male"}
keyname = input("Enter keyname = ")
if keyname in a:
    a.pop(keyname)
    print(a)
else:
    print("key does not exist")
