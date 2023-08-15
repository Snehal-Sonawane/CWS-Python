"""
2 Type of files:
    1. Text file (txt,py,cpp)
    2. Binary File (doc,pdf,mp3,mp4)

3 Types of mode to open a file:
    1. Read
    2. Write
    3. Append
"""
f = open("abc.txt", "r")
r=f.read()
print(r)
s=f.readline() #1st line read
print(s)
# p=f.readline() #2nd line read and print
# print(p)
x = f.readlines()  # all lines read and print
print(x)
f.close()

# Q4. Read a file using python program. Print all the words in a
# reverse order.

s=open("abc.txt","r")
r=s.read()
print(r)
b=r.split()
print(b)
for i in b :
    print(i[::-1])



user_string = "aeroplane ok is a good mode of a transport good bye ok done"
b = user_string.split()
print(b)
for i in b:
    print(i[::-1], end=" ")