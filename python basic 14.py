#list in python intro
a=["parrot", 10,'green', 12.5]
print(a)
print("a[0]=",a[0])
print("a[-2]=",a[-2])
#changing the element in a list
a[1]=100
print("we have changed the value at a[1] to 100 instead of 10")
print(a)
print("------------")


#list slicing
a=["parrot", 10,'green', 12.5]
print(a)
print("------------")
print("a[0:]=",a[0:])
print("------------")
print("a[:]=",a[:])
print("------------")
print("a[1:3]=",a[1:3])
print("------------")
print("a[:3]=",a[:3])
print("------------")
print("a[:4]=",a[:4])
print("------------")
print("a[2::-1]=",a[2::-1])
print("------------")


#updating a list i.e., changing and deletion of elements
a=["parrot", 10,'green', 12.5]
print(a)
print("------------")
print("changing the elements of the list")
print("old a[1]=",a[1])
a[1]='hello'             #changing the elements of the list
print("new a[1]=",a[1])
print("new  list=",a)
print("------------")
print("deleting element in the list")
del a[1]        #we have deleted the element at the a[1]
print("we have deleted the element at the a[1]")
print("new a=",a)
print("------------")


#list traversal=accessing each element of the list indicvidualing or viewing each element
#(METHOD 1)
a=["parrot", 10,'green', 12.5]
print(a)
for i in a:
    print(i)
print("------------")

#(METHOD 2) using the length function in the list
a=["parrot", 10,'green', 12.5]
print(a)
for i in range (len(a)):
    print(a[i])
print("------------")

#(METHOD 2 B) instead of len(a) we wrote directly 4 i.e., the len of the list here
a=["parrot", 10,'green', 12.5]
print(a)
for i in range (4):
    print(a[i])
print("------------")


#functions related to list
# 1
#len()= gives the total length function of the list
print("finding the length of the list")
print("------------")
a=[1,2,3,4,'green',7.8,'yoyo']
print(a)
b=len(a)
print(b)
print("length of the list=",len(a))
print("------------")
print("------------")

# 2
#max()=gives maximum value of the list
# 3
#min()=gives minimum value of the list
print("maximum and minimum value of the list")
print("------------")
a=[10,20,30,50,70,40]
print(a)
b=max(a)
c=min(a)
print("maximum of the list a=",b)
print("minimum of the list a=",c)
print("------------")

#if integer and string both are given
#a=[1,2,3,4,'green',7.8,'yoyo']
#print(a)
#b=max(a)     #TypeError: '>' not supported between instances of 'str' and 'int'
#print("max=",b)

#comparison between string values
#it will be done on the basis of alphabetical order i.e., a=min and z=max 
a=['parrot','green','yoyo']
print(a)
b=max(a)
c=min(a)
print("maximum of the list a=",b)
print("minimum of the list a=",c)
print("------------")
print("------------")

# 4
#list.append(object)=used to add element to the end of the list
print("add element to the list")
print("------------")
#example 1
a=["parrot","green","chilly","red"]
a.append("sky")
print(a)
print("------------")

#example 2
a=[]
for i in range (10):
    x=input("enter the element to add in the list=")
    a.append(x)
print (a)                  #print data horizontally
print("------------")

#example 2b print style is different
a=[]
for i in range (10):
    x=input("enter the element to add in the list=")
    a.append(x)
for i in range (10):
    print(a[i])                          #print data vertically
print("------------")

#example 2c print style is different
a=[]
for i in range (10):
    x=input("enter the element to add in the list=")
    a.append(x)
for i in a:
    print(i)                            #print data vertically
print("------------")

#example 2d print style is different
a=[]
for i in range (10):
    x=input("enter the element to add in the list=")
    a.append(x)
for i in a:
    print(i, end=" ")                     #print data horizontally
print("------------")

#example 2e range is defined by the user and print style is different
m=int(input("enter the range of the list="))
a=[]
for i in range (m):
    x=input("enter the element to add in the list=")
    a.append(x)
for i in a:
    print(i)                     #print data vertically
print("------------")
print("------------")

# 5
#list.count(object)=count the frequency of a given object
print("count the number of times an element occur")
print("------------")
a=[]
for i in range (10):
    x=input("enter the element to add in the list=")
    a.append(x)
print(a)                          #print data horizontally
x=input("enter the element whose frequency you want to find=")
y=a.count(x)
print("frequency of",x,"=",y)
print("------------")
print("------------")

# 6
#list.index(object)=returns the index of the object
print("finding the index of the given element")
print("------------")
#example 1
a=["parrot","green","parrot","red"]
x=a.index("parrot")
print(a)
print("index of parrot=",x)
print("------------")

#example 2
x=int(input("enter the number of elements you want in the list="))
a=[]
for i in range (x):
    y=input("enter the element to add in the list=")
    a.append(y)
print(a)                          #print data horizontally
m=input("enter the element whose index you want to find=")
n=a.index(m)
print("index of",m,"=",n)
print("------------")
print("------------")

# 7
#list.insert(index,value)=insert value at the given index
print("inserting element to the list")
print("------------")
#example 1
a=["parrot",9,"red"]
x=a.insert(2,"chilly")
print(a)
print("------------")

#example 2
x=int(input("enter the number of elements you want in the list="))
a=[]
for i in range (x):
    y=input("enter the element to add in the list=")
    a.append(y)
print("original list=",a)
index=int(input("enter the index where you want to add the value="))
value=input("enter the value that you want to add to the list=")
a.insert(index,value)
print("new list after insertion=",a)
print("------------")
print("------------")

# 8
#list.remove(value)=used to remove lement from the list
#it removes and deletes the first occurrance of the list
print("removing element from the list")
print("------------")
#example 1
a=["parrot", 10,"red","chilly", 9, "parrot"]
a.remove("parrot")
print(a)
print("------------")

#example 2
a=[]
for i in range (5):
    x=input("enter value for the list=")
    a.append(x)
print("original list=",a)
value=input("enter the value to remove from the list=")
a.remove(value)
print("list after removel of the element=",a)
print("------------")
print("------------")
 
# 9
#list.reverse()=reverse the list itself AND  its value cant be stored anywhere
print("reversing a list")
print("------------")
#example 1
a=["parrot", "red", 10, 23,"chilly"]
a.reverse()
print(a)
print("------------")

#example 2
a=[]
for i  in range (5):
    x=input("enter value for the list=")
    a.append(x)
print("original list=",a)
a.reverse()
print("reversed list=",a)
print("------------")
print("------------")

# 10
#list.sort()=sort the elements of the list in ascending order
#for descending write (reverse=True) in the bracket
print("sorting the element present in the list")
print("------------")
#example 1
a=[1,5,6,7,3,4]
a.sort()
print(a)
print("------------")

#example 2
a=[]
for i  in range (5):
    x=input("enter value for the list=")
    a.append(x)
print("original list=",a)
a.sort(reverse=True)
print("list sorted in descending order=",a)
print("------------")
print("------------")

# 11
#list.pop(index)=removes the last element from the list
#removes last element one by one
print("removing the last element from the list")
print("------------")
#example 1
a=[1,5,6,7,3,4]
a.pop()
print(a)
a.pop(2)
print(a)
print("------------")
print("------------")


#EXAMPLE INCLUDING ALL THE LIST FUNCTION
a=[]
x=int(input("enter the range of the list="))
for i  in range (x):
    y=input("enter value for the list=")
    a.append(y)
print("original list=",a)
print("------------")

print("length of the list=",len(a))
print("------------")

#print("maximum value of the list=",max(a))          #TypeError: 'int' object is not callable
print("------------")

#print("minimum value of the list=",min(a))           #TypeError: 'int' object is not callable
print("------------")

m=input("enter the element whose frequency you want to find=")
n=a.count(m)
print("frequency of",m,"=",n)
print("------------")

o=input("enter the element whose index you want to find=")
p=a.index(o)
print("index of",o,"=",p)
print("------------")

index=int(input("enter the index where you want to add the value="))
value=input("enter the value that you want to add to the list=")
a.insert(index,value)
print("new list after insertion=",a)
print("------------")

value1=input("enter the value to remove from the list=")
a.remove(value1)
print("list after removel of the element=",a)
print("------------")

b=a
print("content present in the list a=",a)
print("content present in the list b=",b)
print("------------")

a.reverse()
print("reversed list=",a)
print("------------")

a.sort(reverse=True)
print("list sorted in descending order=",a)
print("------------")

a.pop()
print("after poping the list=",a)
print("------------")

