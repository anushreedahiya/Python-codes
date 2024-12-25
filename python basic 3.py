#print 1 to 10
i=1;
while(i<=10):
    print(i);
    i=i+1;
print("------------")


#print 1 to n
n=int(input("enter the number upto which you want to print="));
i=0;
while(i<=n):
    print(i);
    i=i+1;
print("------------")


#print from 10 to 1
i=10;
while(i>=1):
    print(i);
    i=i-1;
print("------------")


#print from n to 0
n=int(input("enter the number from which you want to print="));
while(n>=0):
    print(n);
    n=n-1;
print("------------")


#sum from 1 to n
n=int(input("enter number upto which you want to find the sum="));
i=1;
sum=0;
while(i<=n):
    sum=sum+i;
    i=i+1;
print("sum=",sum);
print("------------")


#sum of square from 1 to n
n=int(input("enter number upto which you want to find the sum="));
i=1;
sum=0;
while(i<=n):
    sum=sum+(i*i);
    i=i+1;
print("sum=",sum);
print("------------")


#sum of cubes from 1 to n
n=int(input("enter number upto which you want to find the sum="));
i=1;
sum=0;
while(i<=n):
    sum=sum+(i*i*i);
    i=i+1;
print("sum=",sum);
print("------------")


