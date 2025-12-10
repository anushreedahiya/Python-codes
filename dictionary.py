#dictionary= in curly brackets and (key:value) combination, separated by comma
dict1={"parrot":"green",'chilly':"red"}
print("example of dictionary=",dict1)
print("------------")


#accessing item in dictionary=with the help of key name inside a square brackets (METHOD 1)
dict1={"parrot":"green",'chilly':"red"}
print("dictionary=",dict1)
x=dict1["chilly"]
print("accessing a value=",x)

#using the get() function to access the value (METHOD 2)
y=dict1.get("chilly")
print("accessing a value=",y)
print("------------")


#looping through a dictionary
dict1={'brand':'suzuki','model':'dzire','year':2023}
print("dictionary=",dict1)

#(METHOD 1)
print("keys of the dictionary are=")
for x in dict1:
    print(x)                  #it will print the keys of the dictionary
print("------------")

#(METHOD 2)
print("values of the  dictionary are=")
for y in dict1:
    print(dict1[y])           #it will print the values from the dictionary
print("------------")

#(METHOD 3)
#using values() function to return the values of the dictionary
dict1={'parrot':'green','chilly':'red','year':2023}
print("dictionary=",dict1)
for x in dict1.values():
    print (x)
print("------------")

#(METHOD 4)
#using items()function to return the key names and values both alongside
for y in dict1.items():
    print(y)
print("------------")

#(METHOD 5)
#items()= using 2 variables
for a,b in dict1.items():
    print(a, b)
print("------------")


#changing value of the dictionary by referring to its key name
dict1={'parrot':'green','chilly':'red','year':2023}
print("original dictionary=",dict1)
dict1['year']=2020
print("edited dictionary=",dict1)
print("------------")


#checking whether a key exists in the dictionary
dict1={'parrot':'green','chilly':'red','year':2023}
print("original dictionary=",dict1)
if 'parrot' in dict1:
    print('yes, parrot is one of the key of the dictionary')
else:
    print('no, parrot is not a key in the dictionary')
print("------------")
if 'red' in dict1:
    print('yes, red is a key in the dictionary')
else:
    print('no, red is not a key in the  dictionary')
print("------------")


#adding new element to the  dictionary
dict1={'parrot':'green','chilly':'red','year':2023}
print("original dictionary=",dict1)
dict1['sky']='blue'
print("after addinng an element in the dictionary=")
print("new dictionary=",dict1)
print("------------")


#functions used in dictionary
# 1) len()=return the length of the dictionary i.e., the total number of key:value pairs
dict1={'parrot':'green','chilly':'red','year':2023}
print("dictionary=",dict1)
print("length of the dictionary=",len(dict1))
print("------------")

# 2) pop()=removes the element with specified key name
dict1={'parrot':'green','chilly':'red','year':2023}
print("original dictionary=",dict1)
dict1.pop('chilly')
print("dictionary after deletion=",dict1)
print("------------")

# 3) popitem()=removes the last element of the dictionary
dict1={'parrot':'green','chilly':'red','year':2023}
print("original dictionary=",dict1)
dict1.popitem()
print("dictionary after deletion=",dict1)
print("------------")

# 4) del keyword=removes the item with specified key name
dict1={'parrot':'green','chilly':'red','year':2023}
print("original dictionary=",dict1)
del dict1['chilly']
print("dictionary after deletion=",dict1)
print("------------")

# 5) clear keyword=delete all the element present in the dictionary so the dictionary becomes empty
dict1={'parrot':'green','chilly':'red','year':2023}
print("original dictionary=",dict1)
dict1.clear()
print("dictionary after clearing it=",dict1)
print("------------")

# 6) values()=return the values of the dictionary
dict1={'parrot':'green','chilly':'red','year':2023}
print("dictionary=",dict1)
for x in dict1.values():
    print (x)
print("------------")

# 7) items()= to return the key names and values both alongside (METHOD A)
for y in dict1.items():
    print(y)
print("------------")

#(METHOD B)
#items()= using 2 variables
for a,b in dict1.items():
    print(a, b)
print("------------")

# 8) get()=to access the values of the dictionary
dict1={"parrot":"green",'chilly':"red",'year':2023}
print("dictionary=",dict1)
x=dict1.get("chilly")
print("accessing a value=",x)
print("------------")

# 9) copy()=cpoies the dictionary and print key and values both
dict1={"parrot":"green",'chilly':"red",'year':2023}
print("dictionary=",dict1)
x=dict1.copy()
print("copied dictionary at new place=",x)
print("------------")

# 10) fromkeys()=returns dictionary with specified keys and values
x=("parrot","chilly","year")
y=0
dict1=dict.fromkeys(x,y)
print(dict1)
print("------------")

# 11) setdefault()=returns the value of the item with specified key and if it dont exist we can add it too
# (METHOD 1) when setdefault key is already present in the dictionary
dict1={'parrot':'green','chilly':'red','year':2023}
print("dictionary=",dict1)
x=dict1.setdefault("chilly",'pink')
print("default value of the dictionary=",x)
print("------------")

# (METHOD 2) when setdefault key is not present in the dictionary
dict1={'parrot':'green','chilly':'red','year':2023}
print("dictionary=",dict1)
x=dict1.setdefault("sky","blue")
print("default value of the dictionary=",x)
print("------------")

# 12) update()=it inserts the specified item to the dictionary
dict1={'parrot':'green','chilly':'red','year':2023}
print("original dictionary=",dict1)
dict1.update({"sky": "blue"})
print("updated dictionary=",dict1)
print("------------")


#program to store student information and then searching it
student={}                              #empty dictionary
print('Enter student details:')
while True:
    value=int(input("Enter your roll number= "))
    if value in student:
        print("Roll Number Already Exists")
    else:
        name=input("Enter name=")
        student[value]=name
        print("Record added")
    ans=input("Do you want to continue(y/n)?  ")
    if ans in "nN":
        break
#output
print("\nRoll Number   ","Name")
for x,y in student.items():             #items() takes no arguments
    print(x,"\t\t\t   ",y)
#searching a record
print("\nSearch a record")
value1=int(input("Enter roll number="))
if value1 in student:
    print(value1,'\t\t',student[value1])
    print("Record found")
else:
    print("Record not found")
print("------------")
print("------------")



