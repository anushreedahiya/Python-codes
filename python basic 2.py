#max between 2 numbers
a=int(input("enter 1st number="));
b=int(input("enter 2nd number="));
if a>b:
    print("max number=",a);
else:
    print("max number=",b);
print("------------")


#max between 2 numbers
a=int(input("enter 1st number="));
b=int(input("enter 2nd number="));
c=int(input("enter 3rd number="));
if a>b and a>c:
    print("max number=",a);
elif b>a and b>c:
    print("max number=",b);
else:
    print("max number=",c);
print("------------")


#given number is +ve, -ve and zero
a=int(input("enter number="));
if a>0:
    print("positive number");
elif a<0:
    print("negative number");
else:
    print("zero");
print("------------")


#to find middle number in a group of 3 numbers
a=int(input("enter 1st number="));
b=int(input("enter 2nd number="));
c=int(input("enter 3rd number="));
if (a>b and a<c) or (a<b and a>c):
    print("middle number=",a);
elif (b>a and b<c) or (b<a and b>c):
    print("middle number=",b);
else:
    print("middle number=",c);
print("------------")


#grading a child
a=int(input("enter 1st subject marks="));
b=int(input("enter 2nd subject marks="));
c=int(input("enter 3rd subject marks="));
d=int(input("enter 4th subject marks="));
e=int(input("enter 5th subject marks="));
total=a+b+c+d+e;
percent=(total/500)*100;
print("total marks out of 500=",total, "and percentage=",percent);
if percent>=80:
    print ("grade A");
elif percent>=60:
    print("grade B");
elif percent>=40:
    print("grade C");
else:
    print("grade D");
print("------------")


