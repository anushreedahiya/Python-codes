# lambda function=can take any number of arguments but can only have 1 expression
# syntax::    lambda arguments: expression
# EXAMPLE 1 (METHOD 1)
x=lambda a:a+10
print("x=a+10 and a=5")
print(x(5))
print("---------------")


# (METHOD 2)
# writing same function using def function
def add(a):                  #function definition
    return a+10
x=add(5)                     #calling a function
print("a+10 using a def function")
print(x)
print("---------------")


# EXAMPLE 2
# multiple arguments
x=lambda a,b:a*b
print("x=a*b and a=5, b=6")
print(x(5,6))
print("---------------")


# EXAMPLE 3
#adding 3 number using lambda
y=lambda a,b,c :a+b+c
print("x=a+b+c and a=5, b=6, c=2")
print(y(5,6,2))
print("---------------")
print("-----------------")


# filter function= returns an iterator where the items are filtered
#through a function to test if the item is accepted or not
# EXAMPLE 1 (METHOD 1)
ages=[5,12,17,18,24,32]
def myfun(x):                   #function definition
    if x<18:
        return False
    else:
        return True

adults=list(filter(myfun,ages))     #function calling
print("adults with age above 18 or equal=")
for x in adults:
    print(x)
print("-----------------")


#(METHOD 2)
ages=[5,12,17,18,24,32]
adults=filter(lambda a:a>18 , ages)
print("adults with age above 18=")
for x in adults:
    print(x)
print("-----------------")
print("-----------------")


# printing even number
# EXAMPLE 2 (METHOD 1) USING DEF FUNCTION
a=[5,12,17,18,24,32]
def even(x):                   #function definition
    if (x%2==0):
        return True
    else:
        return False

b=list(filter(even,a))     #function calling
print("even number in the list=")
for x in b:
    print(x)
print("-----------------")


# (METHOD 2) USING LAMBDA FUNCTION
a=[5,12,17,18,24,32]
b=filter(lambda y:y%2==0 , a)
print("even number in the list=")
for x in b:
    print(x)
print("-----------------")
print("-----------------")


# map function= it executes a specified function for each item in a iterable
# The item is sent to the function as parameter
# EXAMPLE 1 (METHOD 1)
ages=[5,12,17,18,24,32]
def myfun(x):                   #function definition 1
    if x<18:
        return False
    else:
        return True

def myfun1(x):                  #function definition 2
    return (x*x)

adults=list(filter(myfun,ages))     #function calling 1
print("adults with age above 18 or equal=")
for x in adults:
    print(x)
squares=map(myfun1,adults)
print("square of the ages which are equal to or greater than 18=")
for x in squares:
    print(x)
print("-----------------")

# (METHOD 2)
ages=[5,12,17,18,24,32]
adults=filter(lambda a: a>=18, ages)
squares=list(map(lambda a: a*a, adults))
print("square of the ages which are equal to or greater than 18=")
for x in squares:
    print(x)
print("-----------------")
print("-----------------")

 
# return statement= used to end the execution of the function call
# and returns the result to the caller
# (METHOD 1)
def add(x,y):
    c=x+y
    return c
a=int(input("enter first number="))
b=int(input("enter second number="))
z=add(a,b)
print("addition=",z)
print("-----------------")

# (METHOD 2)
def add(a,b):
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    c=a+b
    return c
sum=add(a,b)
print("addition=",sum)
print("-----------------")
print("-----------------")




