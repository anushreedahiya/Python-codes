#sum of elements of the list
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
sum=0
for i in range(x):
    sum=sum+a[i]
print("sum of list elements=",sum)
print("------------")


#count the total number of even and odd number in the list
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
even=0
odd=0
for i in range(x):
    if(a[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print("total even=",even)
print("total odd=",odd)
print("------------")


#sum of even number and product of odd number
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
even=0
odd=1
for i in range(x):
    if(a[i]%2==0):
        even=even+a[i]
    else:
        odd=odd*a[i]
print("sum of even number=",even)
print("product of odd number=",odd)
print("------------")


#search a number in the list (METHOD 1)
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
search=int(input("enter the number that you want to search in the list="))
flag=0
position=0
for i in range (x):
    if (a[i]==search):
        flag=1
        position=i+1
        break
if(flag==1):
    print("nummber found in the list at position=",position)
else:
    print("number not found")
print("------------")


#search a number in the list (METHOD 2)
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
search=int(input("enter the number that you want to search in the list="))
for i in range (x):
    if (a[i]==search):
        print("number found")
    else:
        print("number not found")
print("------------")


#to count frequency of a given number
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
val1=int(input("enetr number to find frequency="))
count=0
for i in range (x):
    if (a[i]==val1):
        count=count+1
print("frequency of the number=",count)
print("------------")


#to find maximum number of the list
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
max=a[0]
for i in range (x):
    if (a[i]>max):
        max=a[i]
print("maximum number=",max)
print("------------")


#to find minimum number of the list
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
min=a[0]
for i in range (x):
    if (a[i]<min):
        min=a[i]
print("minimum number=",min)
print("------------")


#to reverse the list itself (CONCEPT OF SWAPPING IS USED)
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
i=0
j=x-1
while(i<j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    i=i+1
    j=j-1
print("reversed list=",a)
print("------------")


#to find min and second min number of the list  (METHOD 1)
#a=[]
#x=int(input("enter how many elements you want in the list="))
#for i in range(x):
#    val=int(input("enter number="))
#    a.append(val)
#print("list=",a)
#minval=min(a)  
#print("min value of the list=",minval)    TypeError: 'int' object is not callable
#a.remove(minval)
#smin=min(a)
#print("second min value of the list=",smin)
#print("------------")


#to find min and second min number of the list  (METHOD 2)
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
a.sort()
print("list after sorting in ascending order=",a)
print("min value of the list=",a[0])
print("second min value of the list=",a[1])
print("------------")


#to find max and second max number of the list  (METHOD 1)
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
a.sort(reverse=True)
print("list after sorting in descending order=",a)
print("max value of the list=",a[0])
print("second max value of the list=",a[1])
print("------------")


#to shift each element of the list to left
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
t=a[0]
for i in range(1,x):
    a[i-1]=a[i]
a[x-1]=t
print("new list=",a)
print("------------")


#to shift each element of the list to right
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
t=a[x-1]
for i in range (x-2,-1,-1):
    a[i+1]=a[i]
a[0]=t
print("new list=",a)
print("------------")


#to insert a number at given position in the list   (index=position-1)
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
position=int(input("enter the position where u want to add the element="))
insert=int(input("enter the value u want to add="))
a.append(None)
for i in range (x-1,position-2,-1):
    a[i+1]=a[i]
a[position-1]=insert
print("list after insertion=",a)
print("------------")


#to delete an element from the list
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
delete=int(input("enter the number that you want to delete="))
flag=0
for i in range(x):
    if(a[i]==delete):
        flag=1
        position=i
        break
if(flag==0):
    print("number not found")
else:
    for i in range(position, x-1):
        a[i]=a[i+1]
    a.pop()
    print("list after deleting the number=",a)
print("------------")


#to shift each element of the list to left by 'n' position
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
n=int(input("enter the position by which the number shift towards left="))
for j in range (n):
    t=a[0]
    for i in range(1,x):
        a[i-1]=a[i]
    a[x-1]=t
print("new list=",a)
print("------------")


#to shift each element of the list to right by 'n' position
a=[]
x=int(input("enter how many elements you want in the list="))
for i in range(x):
    val=int(input("enter number="))
    a.append(val)
print("list=",a)
n=int(input("enter the position by which the number shift towards right="))
for j in range (n):
    t=a[x-1]
    for i in range (x-2,-1,-1):
        a[i+1]=a[i]
    a[0]=t
print("new list=",a)
print("------------")



