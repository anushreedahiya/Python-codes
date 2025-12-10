#tuple declaration
tuple1=(1,2,3,"parrot","green")
print("tuple=",tuple1)
print("------------")


#tuple=immutable
#tuple1[0]=10         TypeError: 'tuple' object does not support item assignment
#print("new tuple=",tuple1)


#occupy less memory than list
import sys           #library in which getsizeof function is present
list1=[1,2,3,"parrot","green"]
tuple1=(1,2,3,"parrot","green")
print("size of list=",sys.getsizeof(list1))     #answer=96
print("size of tuple=",sys.getsizeof(tuple1))   #answer=80
print("------------")


#list takes more time in comparison to tuple
import timeit           #library
list1=timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,0,'parrot']", number=1000)
tuple1=timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,0,'parrot')",number=1000)
print("time taken by list to execute=",list1)
print("time taken by tuple to execute=",tuple1)
print("------------")


#creating tuple
tuple1=(2)     #act like an integer as in tuple after single element also a comma should be there
tuple2=(2,)    #single element tuple
print(tuple1)
print(tuple2)
print("------------")


#creating tuple from strings
t1=tuple('world')
t2=tuple("world")
print(t1)
print(t2)
print("------------")

#creating tuple from a list
list1=[1,2,3,4,5]
t1=tuple(list1)
print("list=",list1)
print("tuple=",t1)
print("------------")


#different types of tuple
t1=()                                         #empty tuple
print("empty tuple=",t1)
t2=(23,)                                      #single element tuple
print("single element tuple=",t2)
t3=(1,2,3,4)                                  #integer tuple
print("integer tuple=",t3)
t4=(1,2,3.5,5,4)                              #number tuple
print("number tuple=",t4)
t5=('a',"n",'d')                              #character tuple
print("character tuple=",t5)
t6=('a',1,2,3.5,5,'parrot')                   #mixed data type tuple
print("mixed data type tuple=",t6)
t7=('parrot','green',"red")                   #string tuple
print("string tuple=",t7)
print("------------")


#traversing tuple
#type 1
tuple1=(1,2,3,4,5)
for i in tuple1:
    print(i)                                #print the elements vertically
print("------------")

#type 2
tuple1=(1,2,3,4,5)
for i in range(len(tuple1)):
    print(tuple1[i])                       #print the elements vertically
print("------------")


#joining tuple
tuple1=(1,2,3,4,5)
tuple2=(6,7,8)
tuple3=tuple1+tuple2
print("tuple1=",tuple1)
print("tuple2=",tuple2)
print("combination of tuple 1 and tuple 2=",tuple3)
print("------------")


#repeating or replicating tuples
tuple1=(1,2,3,4)
tuple2=tuple1*3
print("tuple1=",tuple1)
print("replicating tuple1 thrice=",tuple2)
print("------------")


#slicing the tuple [start:stop:step value] by default step value=1
tuple1=(10,11,12,13,14,15)
tuple2=tuple1[3:5]
print("tuple1=",tuple1)
print("tuple after slicing [3:5]=",tuple2)
tuple3=tuple1[0:5:2]
print("tuple after slicing [0:5:2]=",tuple3)
print("------------")


#tuple method/functions
# 1) len(<tuple>)=returns length of the tuple
employee=("parrot","cat",408,107)
print("employee=(name of tuple)=",employee)
print("length of the tuple employee=",len(employee))
print("------------")

# 2) max()=returns the max value of the tuple
a=(10,20,30,40,25,15,75)
print("tuple=",a)
print("max value of the tuple=",max(a))
print("------------")

# 3) min()=returns the min value of the tuple
a=(10,20,30,40,25,15,75)
print("tuple=",a)
print("min value of the tuple=",min(a))
print("------------")

# 4) index()=returns the index of an existing element in the tuple
#syntax   =   <tuple name>.index(<item>)
a=(10,20,30,40,25,15,75)
print("tuple=",a)
print("index of 30=",a.index(30))
print("------------")

# 5) count()=returns the frequency of given element
#syntax   =   <tuple name>.count(<element>)
a=(10,20,30,40,25,15,75,20)
print("tuple=",a)
print("count of 20=",a.count(20))
print("------------")

# 6) tuple()=used as a constructor which is used to create tuples from different type of values
#syntax   =   tuple(<sequence>)
print("empty list=",tuple())
print("------------")
t=tuple([1,2,3])
print("tuple from a list=",t)
print("------------")
t1=tuple("parrot")
print("tuple from string=",t1)
print("------------")
t2=tuple({1:"m",2:"n"})
print("tuple from key of dictionary=",t2)
print("------------")


#tuple manipulation (TUPLE --->LIST then again LIST--->TUPLE)
x=("parrot","green","chilly")
print("original tuple=",x)
y=list(x)                             #converting the tuple to list to change it
print("so called list=",y)
y[2]="red"                            #changing the list that was once a tuple
x=tuple(y)                            #changing list back to tuple
print("our ner tuple=",x)
print("------------")


#check if items exist in the tuple use "in"
tuple1=("parrot","green","chilly","red")
if "green" in tuple1:
    print("yes element exist in the tuple")
else:
    print("no element dont exist in the tuple")
print("------------")


#delete tuple element=not possible but can delete whole tuple
tuple1=("parrot","green","chilly","red")
print("tuple=",tuple1)
del(tuple1)
#print("after deleting the tuple=",tuple1)           #NameError: name 'tuple1' is not defined
print("------------")

