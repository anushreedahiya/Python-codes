#using function
def factorial(i):
    if i==1:
        return 1
    else:
        return (i*factorial(i-1))
    
number=int(input("enter the number="))
print("The factorial of", number, "is", factorial(number))

