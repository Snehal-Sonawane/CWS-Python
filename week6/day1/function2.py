def number():
    a=int(input("Enter start num = "))
    b=int(input("Enter end num = "))
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    print(sum)    

number()