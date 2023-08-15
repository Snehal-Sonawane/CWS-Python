try:
    name=input("Enter a name = ")
    password=input("Enter a pass = ")
    if name=="admin" and password=="admin":
        print("your successfully logged in")
    else:
        raise Exception ("wrong password")    
except Exception as e:
    print(e)  