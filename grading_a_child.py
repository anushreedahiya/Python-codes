#grading
sub1=int(input("enter marks of 1st subject "))
sub2=int(input("enter marks of 2nd subject "))
sub3=int(input("enter marks of 3rd subject "))
sub4=int(input("enter marks of 4th subject "))
sub5=int(input("enter marks of 5th subject "))
average=float((sub1+sub2+sub3+sub4+sub4+sub5)/5)
if average>=90:
    print("Grade:A")
elif average>=80 and average<=90:
    print("Grade:B")
elif average>=70 and average<=80:
    print("Grade:C")
elif average>=60 and average<=70:
    print("Grade:D")
else:
    print("Grade:F")



#score grade
score=float(input("enter the score "))
if score<=1 and score>=0.9:
    print("grade obtained is A")
elif score>=0.8 and score<0.9:
    print("grade obtained is B")
elif score>=0.7 and score<0.8:
    print("grade obtained is C")
elif score>=0.6 and score<0.7:
    print("grade obtained is D")
else:
    print("grade obtained is F")
