# Q1. Ask a sentence from the user. Count the number of words in a
# sentence using split() method.
s1 = input("Enter a sen = ")
b = s1.split()
print(b)
print(len(b))

# Q2. Ask a sentence from the user. Count the number of vowels in
# that sentence.
s1 = input("Enter a sen = ")
vowels = 0
for i in s1:
    if i.isalpha():
        if i in "aeiou":
            vowels = vowels + 1
print(vowels)

# Q3. Write a program to find the longest word in a given string and
# print the word.

a = "snehal sonawane is a  great student"
b = a.split()
maxi = 0
name = True
print(b)
for i in b:
    print(len(i))
    if len(i) > maxi:
        maxi = len(i)
        name = i
print(f"Max length of word is {maxi} word is {name}")

# Q4. Write a program to find the shortest word in a given string and
# print the word. Make sure that all the words are of different length
# in the string.


a = "snehal sonawane is a  great student"
b = a.split()
mini = b[0]
for i in range(1, len(b)):
    if a[i] < mini:
        mini = a[i]
print(mini)

#  Q5. Write a program to create a new string by swapping the first
# and last characters of a given string. If the string has only one
# character, print the original string.


# Q6. Write a program to remove all spaces from a given string and
# print the resulting string.

a = "   sonawanesnehal 1142@gmail.com  "
b = a.replace(" ", "")
print(b)

# Q7. Write a program to concatenate two given strings without
# using the + operator and print the result. (Hint: Store 2 strings in list,
# and print using join method)

a = "snehal"
b = "sonawane"
c = list(a)
d = list(b)
p = []
for i in c:
    p.append(i)
for i in d:
    p.append(i)
s1 = "".join(i for i in p)
print(s1)

# Q8. Write a program that takes a string as input and prints the
# string with its first letter capitalized and the rest of the string in
# lowercase.

a = input("Enter a string = ")
b = a.capitalize()
print(b)

# Q9. Write a program to check if a given string contains any digits
# and print "Contains digits" if it does, otherwise print "Does not
# contain digits"

a = "ab1234"
b = 0
for i in a:
    if i.isdigit():
        b = b + 1
if b > 0:
    print("yes")
else:
    print("no")

#  Q10. Write a program to replace all the spaces with “-” character.
# Use replace() method.

a = "snehal avinash sonawane"
b = a.replace(" ", "-")
print(b)

# Q11. Ask a sentence from user. Then ask a letter from user. Remove
# all the letter from the sentence entered by user and print the result.


a = input("Enter a string = ")
b = input("Enter a letter = ")
for i in a:
    res = a.replace(b, "")
print(res)
