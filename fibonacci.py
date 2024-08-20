n=int(input("enter the number"))
a,b=0,1
while n>=0:
    c=a+b
    a=b
    b=c
    print(c)
    n=n-1


n=int(input("enter the number for fibonacci series= "))
a,b=0,1
print(a,b,end="")
for i in range (3,n+1):
    c=a+b
    print (c,end="")
    a=b
    b=c
    

def fibonacci(n):
    f=[0,1]

n=int(input("enter the number"))
for i in range (2, n+1):
    f.append(f[i-1]+f[i-2])
    return(f[n])

print(fibonacci[n])

