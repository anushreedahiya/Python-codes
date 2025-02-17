# A     Printing star in inverted Right Angle Triangle Shape
i=1;                                     # *****
while i<=5:                              # ****
    b=1;                                 # *** 
    while b<=6-i:                        # **
        print("*",end='')                # *     no space in end
        b=b+1;
    j=1
    while j<=i:
        print(" ",end='') #no space in the end
        j=j+1
    print ( )
    i=i+1
print("------------")
#here j potion is doing the printing of the space and b potion printing the stars


# B     Printing number in inverted Right Angle Triangle Shape
i=1;                                     # 11111
while i<=5:                              # 2222
    b=1;                                 # 333
    while b<=6-i:                        # 44
        print(i,end='')                  # 5    no space in end
        b=b+1;
    j=1
    while j<=i:
        print(" ",end='') #no space in the end
        j=j+1
    print ( )
    i=i+1
print("------------")


# C     Printing number in inverted Right Angle Triangle Shape
i=1;                                     # 12345
while i<=5:                              # 1234
    b=1;                                 # 123
    while b<=6-i:                        # 12
        print(b,end='')                  # 1   no space in end
        b=b+1;
    j=1
    while j<=i:
        print(" ",end='') #no space in the end
        j=j+1
    print ( )
    i=i+1
print("------------")


# A      Printing Stars '*' in Opposite Pyramid Shape
n=int(input("enter the number of rows="))          # *********   for n=5
i=1                                                # -*******
while n>0:                                         # --*****
    b=1                                            # ---***
    while b<i:                                     # ----*
        print (" ",end='')
        b=b+1
    j=1
    while (j<=(n*2)-1):
        print ("*", end='')
        j=j+1
    print()
    n=n-1
    i=i+1
print("------------")


#  B      Printing number in Opposite Pyramid Shape
n=int(input("enter the number of rows="))          # 111111111   for n=5
i=1                                                # -2222222
while n>0:                                         # --33333
    b=1                                            # ---444
    while b<i:                                     # ----5
        print (" ",end='')
        b=b+1
    j=1
    while (j<=(n*2)-1):
        print (i, end='')
        j=j+1
    print()
    n=n-1
    i=i+1
print("------------")


#   C    Printing number in Opposite Pyramid Shape
n=int(input("enter the number of rows="))          # 123456789   for n=5
i=1                                                # -1234567
while n>0:                                         # --12345
    b=1                                            # ---123
    while b<i:                                     # ----1
        print (" ",end='')
        b=b+1
    j=1
    while (j<=(n*2)-1):
        print (j, end='')
        j=j+1
    print()
    n=n-1
    i=i+1
print("------------")


#   D    Printing number in Opposite Pyramid Shape
n=int(input("enter the number of rows="))          # 555555555   for n=5
i=1                                                # -4444444
while n>0:                                         # --33333
    b=1                                            # ---222
    while b<i:                                     # ----1
        print (" ",end='')
        b=b+1
    j=1
    while (j<=(n*2)-1):
        print (n, end='')
        j=j+1
    print()
    n=n-1
    i=i+1
print("------------")


