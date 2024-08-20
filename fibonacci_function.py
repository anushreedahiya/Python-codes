# using function
def fibonacci(n):
    f=[0,1]

n=int(input("enter the number"))
for i in range (2, n+1):
    f.append(f[i-1]+f[i-2])
    return(f[n])

print(fibonacci[n])
