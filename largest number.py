a=float(input("enter 1st number "))
b=float(input("enter 2nd number "))
c=float(input("enter 3rd number "))
if a>=b and a>=c:
    print("largest number is ",a)
elif b>=a and b>=c:
    print("largest number is ",b)
else:
    print("largest number is ",c)