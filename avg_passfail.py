#whether child pass or not
sub1=int(input("enter marks of 1st subject "))
sub2=int(input("enter marks of 2nd subject "))
sub3=int(input("enter marks of 3rd subject "))
sub4=int(input("enter marks of 4th subject "))
sub5=int(input("enter marks of 5th subject "))
average=float((sub1+sub2+sub3+sub4+sub4+sub5)/5)
if average>=40:
    print("Grade:Pass")
else:
    print("Grade:Fail")



#if child pass in a subject
sub1=int(input("enter marks of 1st subject "))
sub2=int(input("enter marks of 2nd subject "))
sub3=int(input("enter marks of 3rd subject "))
sub4=int(input("enter marks of 4th subject "))
sub5=int(input("enter marks of 5th subject "))
average=float((sub1+sub2+sub3+sub4+sub4+sub5)/5)
if sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40 and sub5>=40:
    print("Grade:Pass")
    print("average is ",average)
else:
    print("Grade:Fail")
    print("average is ",average)    
