n=int(input("enter a number= "))
factorial=1
if n<0:
    print("factorial doesn't exist")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1, n+1):
        factorial=factorial*i
    print("factorial of ",n,"is", factorial)



#using function
def factorial(i):
    if i==1:
        return 1
    else:
        return (i*factorial(i-1))
    
number=int(input("enter the number="))
print("The factorial of", number, "is", factorial(number))

