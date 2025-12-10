#function calling and definition
def message():              #function definition
    print("hello world")

message()       #function calling
message()
print("------------")


#adding 2 number using function without argument
def add():                  #function definition
    a=int(input("enter first number for addition="))
    b=int(input("enter second number for addition="))
    c=a+b
    print("addition=",c)

add()       #function calling
add()
print("------------")
#for each function calling we will give input and can get different output


#with argument basic example
def addition(a,b):
    c=a+b
    print("addition=",c)

addition(5,6)
print("------------")


#addition of 2 number user input and function with argument 
a=int(input("enter first number for addition="))
b=int(input("enter second number for addition="))
addition(a,b)

def addition(a,b):
    c=a+b
    print("addition=",c)

print("------------")
#function can be defined before the main body after it no difference in the result


#addition of 2 number user input and function with argument
def addition(a,b):
    c=a+b
    print("addition=",c)

a=int(input("enter first number for addition="))
b=int(input("enter second number for addition="))
addition(a,b)
print("------------")


#odd even number without argument
def oddeve():    #function definition
    a=int(input("enter the number to find if its odd or even="))
    if(a%2==0):
        print("even number")
    else:
        print("odd number")

oddeve()   #calling function
print("------------")


#odd even number with argument
def oddeve(a):    #function definition
    if(a%2==0):
        print("even number")
    else:
        print("odd number")

x=int(input("enter the number to find if its odd or even="))
oddeve(x)   #calling function
print("------------")


#types of function
#no argument no return
print("no argument no return")
def add():
    a=int(input("enter first number for addition="))
    b=int(input("enter second number for addition="))
    c=a+b
    print("sum=",c)     #no return statement

add()   #no argument
print("------------")


#with argument no return
print("with argument no return")
def add(a,b):
    c=a+b
    print("sum=",c)     #no return statement instead print statement is given

x=int(input("enter first number for addition="))
y=int(input("enter second number for addition="))
add(x,y)   #argument is given
print("------------")


#no argument with return
print("no argument with return")
def add():
    a=int(input("enter first number for addition="))
    b=int(input("enter second number for addition="))
    c=a+b
    return(c)     #return statement given therefore no print statement

x=add()   #no argument and return statement is stored here
print("sum=",x)    #the place where return statement was stored is printed
print("------------")

 
#with argument with return
print("with argument with return")
def add(a,b):
    c=a+b
    return(c)     #return statement is given

x=int(input("enter first number for addition="))
y=int(input("enter second number for addition="))
z=add(x,y)   #argument is given
print("sum=",z)
print("------------")


#default argument
def add(a,b,c=5):
    d=a+b+c
    print("sum=",d)

add(5,6,7)
add(5,6)
print("------------")


#after default argument every value will be given a default value otherwise error
#def add(a,b,c=5,d):   (SyntaxError: non-default argument follows default argument)
#    e=a+b+c+d
#    print("sum=",e)
#
#add(3,4, ,6)   (SyntaxError: invalid syntax)


def add(a=6,b=7,c=5):
    d=a+b+c
    print("sum=",d)

add()
add(10)
add(10,20)
add(10,20,30)
print("------------")


#break and continue statement
print("break statement")
i=1
while (i<=5):
    if (i==3):
        break
    print(i)
    i=i+1
print("------------")

print("continue statement")
i=0
while (i<=5):
    i=i+1
    if (i==3):
        continue
    print(i)
print("------------")


