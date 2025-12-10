#for loop function snippet code to print 1 to 10
for i in range (1, 11):
    print (i)
print("------------")


#for loop function snippet code to print 1 to 10
for i in range (1, 11):
    print (i)
else:
    print ("program terminated")
print("------------")


#for loop function snippet code to print 10 to 1
for i in range (10, 0,-1):
    print (i)
print("------------")


#for loop function snippet code to print table of 2
for i in range (2, 21, +2):
    print (i)
print("------------")


#to print table of 3
for i in range (3, 31, +3):
    print (i)
print("------------")


#to print table of a given number (METHOD 1)
n=int(input("enter the number whose table you want to find="))
for i in range (n, (10*n)+1, +n):
    print (i)
print("------------")


#to print table of a given number (METHOD 2)
n=int(input("enter the number whose table you want to find="))
for i in range (1, 11):
    print (i*n)
print("------------")


#to print table of a given number (METHOD 3)
n=int(input("enter the number whose table you want to find="))
i=1
while i<=10:
    print (i*n)
    i=i+1
print("------------")


