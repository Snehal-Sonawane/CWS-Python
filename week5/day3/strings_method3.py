# letter present in string if yes print yes or no
a = input("Enter a sentance = ")
b = input("Enter a letter = ")

if a.find == -1:
    print("no")
else:
    print("yes")

# 2nd method
a = input("Enter a sentance = ")
b = input("Enter a letter = ")
if a.find != -1:
    print("yes")
else:
    print("no")


"""
Ask sentence
Ask letter


If letter exists
    Then only ask new letter
    Then replace old letter with new letter

Else
    Print does not exists
"""
sen = input("Enter a sen= ")
letter = input("Enter a letter= ")
if sen.find != -1:
    new_letter = input("Enter new letter = ")
    result = sen.replace(letter, new_letter)
    print(result)
else:
    print("no")

# 2nd method
user_string = input("Enter a sentence = ")
letter = input("Enter a letter = ")

if letter in user_string:
    new_letter = input("Enter new letter = ")
    result = user_string.replace(letter, new_letter)
    print(result)
else:
    print("Does not exists")
