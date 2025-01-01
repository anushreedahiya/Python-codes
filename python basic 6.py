#to find the product of digits of a given number
n=int(input("enter number to find its product of the digits="));
prod=1;
while(n>0):
    prod=prod*(n%10);
    n=n//10;
print("product of digits=",prod);
print("------------")


#to find the sum of even number and product of add digits of a number
i=int(input("enter the number="))
sum=0
product=1
while(i>0):
    x=i%10
    if x%2==0:
        sum=sum+x
    else:
        product=product*x
    i=i//10
print("sum nof even number=",sum)
print("product of odd number=",product)
print("------------")


#reverse of a given number
n=int(input("enter number to find its reverse="));
rev=0;
while (n>0):
    rev=(rev*10)+(n%10);
    n=n//10;
print("reverse of number=",rev);
print("------------")


#given number is palindrome or not
n=int(input("enter number to see if it is palindrome or not="));
rev=0;
i=n;
while (i>0):
    rev=(rev*10)+(i%10);
    i=i//10;
print("reverse of number=",rev);
if(rev==n):
    print("palindrome number");
else:
    print("not palindrome number");
print("------------")


#to check if given number is prime or composite
n=int(input("enter the number to see if it is prime or composite="));
count=0;
i=1;
while(i<=n):
    if(n%i==0):
        count=count+1;
    i=i+1;
if(count==2):
    print("prime number");
else:
    print("composite number");
print("------------")

        
#to print factorial of a number
n=int(input("enter number to find its factorial="));
fact=1;
while(n>0):
    fact=fact*n;
    n=n-1;
print("factorial=",fact);
print("------------")


#to print fibonacci series upto a given number
n=int(input("enter number to print fibonacci series="));
x=0;
y=1;
z=0;
while(z<=n):
    print(z);
    x=y;
    y=z;
    z=x+y;
print("------------")



