#print even numbers between 1 to n (METHOD1)
n=int(input("enter number upto which you want to print="));
i=2;
while(i<=n):
    print(i);
    i=i+2;
print("------------")


#print even numbers between 1 to n (METHOD2)
n=int(input("enter number upto which you want to print="));
i=2;
while(i<=n):
    if i%2==0:
        print(i);
    i=i+1;
print("------------")


#to find sum of even number from 1 to n (METHOD 1)
n=int(input("enter number upto which you want to add even number="));
i=2;
sum=0;
while(i<=n):
    sum=sum+i;
    i=i+2
print("sum of even numbers=", sum);
print("------------")


#to find sum of even number from 1 to n (METHOD 2)
n=int(input("enter number upto which you want to add even number="));
i=1;
sum=0;
while(i<=n):
    if (i%2==0):
        sum=sum+i;
    i=i+1
print("sum of even numbers=", sum);
print("------------")


#to find the sum of first n even numbers
n=int(input("number of even numbers you want to add="));
i=1;
sum=0;
count=0;
while(count<=n):
    if (i%2==0):
        sum=sum+i;
        count=count+1;
    i=i+1;
print("sum of even numbers=",sum);
print("------------")

