#string basic example (METHOD 1)
name="parrot"                  #parrot   output in this form
print(name)
print("------------")


#initialization of string (METHOD 2)
name="parrot"                      #p   output in this form
for i in name:                     #a
    print (i)                      #r
print("------------")


#initialize (METHOD 3)
name="parrot"                      #parrot    output in this form
for i in name:
    print(i,end="")
print()
print("------------")


#string operators
print("concatenation (+)")
a="every"+"day"
x="every"
y="day"
z=x+y
print(a)
print(z)
print("------------")

print("replication (*)")
x=3*"hello"
print(x)
print("------------")

print("membership( in /not in)")
x="ram"
if ("a" in "ram"):
    print("true")
print("------------")

x="ram"
if ("x" not in "ram"):
    print("true")
print("------------")

print("comparison (<,<=,>,>=,==,!=)")
x="ram"
y="RAM"
if(x==y):
    print("true")
else:
    print("false")
print("------------")


#string slicing
a="hello world"
print("a[4:-2]=",a[4:-2])
print("a[6:], a[:6]=",a[6:], a[:6])
print("a[6:10]=",a[6:10])
print("a[6:]=",a[6:])
print("a[3:-2]=",a[3:-2])
print("a[:5]=",a[:5])
print("------------")


#string built in function
print("len()=length of the string")
a=input("enter the text to find its length=")
print(len(a))
print("------------")
print("capitalize()=first letter is capitalized")
print(a.capitalize())
b=a.capitalize()
print(b)
print("------------")
print("find()=returns the index of the lowest digit if found in the string")
a=input("enter the string=")
b=input("enter the substring you want to find=")
print(a.find(b,0,(len(a)-1)))
print("------------")
print("isalnum()=returns true if character or numbers or both are there")
print("isdigit()=returns true for only number entrys")
print("isspace()=returns true for only white space")
a="parrot13"
print("isalnum=",a.isalnum())
print("isdigit=",a.isdigit())
print("isspace=",a.isspace())
print("------------")
b="number"
print("isalnum=",b.isalnum())
print("isdigit=",b.isdigit())
print("isspace=",b.isspace())
print("------------")
c="123"
print("isalnum=",c.isalnum())
print("isdigit=",c.isdigit())
print("isspace=",c.isspace())
print("------------")
d=""
print("isalnum=",d.isalnum())
print("isdigit=",d.isdigit())
print("isspace=",d.isspace())
print("------------")
e=" "
print("isalnum=",e.isalnum())
print("isdigit=",e.isdigit())
print("isspace=",e.isspace())
print("------------")
f="parrot "
print("isalnum=",f.isalnum())
print("isdigit=",f.isdigit())
print("isspace=",f.isspace())
print("------------")


#printing string using looping (METHOD 1)
a=input("enter the text to print it=")
for i in range (0,len(a)):
    print(a[i])
print("------------")

#printing string using looping (METHOD 2)
a=input("enter the text to print it=")
for i in range (0,len(a)):
    print(a[i],end="")
print()
print("------------")


#reverse of the string (METHOD 1)
a=input("enter the text you want to reverse=")
print(a[-1::-1])
print("------------")


#reverse of the string (METHOD 2)
a=input("enter the text you want to reverse=")
for i in range ((len(a)-1), -1, -1):
    print(a[i],end="")
print()
print("------------")


#counting the number of vowels and consonants
a=input("enter the text=")
vowel=0
cons=0
for i in range (0,len(a)):
    if(a[i]!=' '):
    #space is given in single quotation as space is neither consonant nor vowel
        if (a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u"
        or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
            vowel=vowel+1
        else:
            cons=cons+1
print("total number of vowels=",vowel)
print("total number of consonants=",cons)
print("------------")


#palindrome string using in built function
a=input("enter the text to find if its palindrome or not=")
b=a[-1: :-1]
print("reverse string=",b)
if(a==b):
    print("palindrome string")
else:
    print("not palindrome string")
print("------------")


