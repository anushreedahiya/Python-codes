#to find the sum of digits of a given number
n=int(input("enter the number to find the sum of digits="));
sum=0;
while(n>0):
    sum=sum+n%10;
    n=n//10;
print("sum of digits=",sum);
print("------------")


#to find the sum of square of digits of a given number
n=int(input("enter the number to find the sum of square of digits="));
sum=0;
while(n>0):
    sum=sum+(n%10)**2;
    n=n//10;
print("sum of square of digits=",sum);
print("------------")


#to find the sum of cube of digits of a given number
n=int(input("enter the number to find the sum of cube of digits="));
sum=0;
while(n>0):
    sum=sum+(n%10)**3;
    n=n//10;
print("sum of cube of digits=",sum);
print("------------")


#to check if given number is armstrong number (3 digit number)
n=int(input("enter the number to check if it is an armstrong number="));
i=n;
sum=0;
while(n>0):
    sum=sum+(n%10)**3;
    n=n//10;
print("sum of cube of digits=",sum);
if (sum==i):
    print("armstrong number");
else:
    print("not armstrong number");
print("------------")


#to check armstrong number of any digit number (METHOD 1)
n=int(input("enter any digit number to see if its armstrong="));
i=n;
count=0;
while(i>0):
    i=i//10;
    count=count+1;
i=n;
sum=0;
while(i>0):
    digit=i%10;
    x=1;
    prod=1;
    while(x<=count):
        prod=prod*digit;
        x=x+1;
    sum=sum+prod;
    i=i//10;
print("sum of digits=",sum);
if(sum==n):
    print("armstrong number");
else:
    print("not armstrong number");
print("------------")


#to check armstrong number of any digit number (METHOD 2)
n=int(input("enter any digit number to see if its armstrong="));
i=n;
count=0;
while(i>0):
    i=i//10;
    count=count+1;
i=n;
sum=0;
while(i>0):
    sum=sum+(i%10)**count;
    i=i//10;
print("sum of digits=",sum);
if(sum==n):
    print("armstrong number");
else:
    print("not armstrong number");
print("------------")


