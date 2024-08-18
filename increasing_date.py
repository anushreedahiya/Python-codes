my_date=input("enter a date")
dd,mm,yy=my_date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max_value=31
elif (mm==4 or mm==6 or mm==9 or mm==11):
    max_value=30
elif (yy%4==0 and yy%100==0 and yy%400==0):
    max_value=29
else:
    max_value=28

if (mm<1 or mm>12 or dd<1 or dd>max_value):
    print("invalid data")
elif(dd==max_value and mm!=12):
    dd=1
    mm=mm+1
    print("incremented date is=", dd, mm, yy)
elif(dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print("incremented date is=", dd, mm, yy)
else:
    dd=dd+1
    print("incremented date is=",dd ,mm, yy)
    
