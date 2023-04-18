a=int(input("Enter any no:\n"))
b=int(input("Enter any no:\n"))
c=int(input("Enter any no:\n"))
d=int(input("Enter any no:\n"))
if(a>b and a>c and a>d):
    print("The greatest Number is: ",a)
elif(b>a and b>c and b>d):
    print("The greatest number is: ",b)
elif(c>a and c>b and c>d):
    print("The greatest number is: ",c)
elif(d>a and d>b and d>c):
    print("The greatest number is: ",d)
else:
    print("null")