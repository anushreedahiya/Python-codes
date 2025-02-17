# A     Printing Stars '*' in reverse Right Angle Triangle Shape
i=1;                                     #     *
while i<=5:                              #    **
    b=1;                                 #   ***
    while b<=5-i:                        #  ****
        print(" ",end='')                # *****     no space in end
        b=b+1;
    j=1
    while j<=i:
        print("*",end='') #no space in the end
        j=j+1
    print ( )
    i=i+1
print("------------")


#   B       Printing number reverse Right Angle Triangle Shape
i=1;                                     #     1
while i<=5:                              #    22
    b=1;                                 #   333
    while b<=5-i:                        #  4444
        print(" ",end='')                # 55555     no space in end
        b=b+1;
    j=1
    while j<=i:
        print(i,end='') #no space in the end and i is in print
        j=j+1
    print ( )
    i=i+1
print("------------")


#C    Printing number reverse Right Angle Triangle Shape
i=1;                                     #     1
while i<=5:                              #    12
    b=1;                                 #   123
    while b<=5-i:                        #  1234
        print(" ",end='')                # 12345     no space in end
        b=b+1;
    j=1
    while j<=i:
        print(j,end='') #no space in the end and "j"  is in the print
        j=j+1
    print ( )
    i=i+1
print("------------")


# A    Printing Stars '*' in Pyramid Shape
k=1                                   # ----*      4 space and 1 star
i=1                                   # ---***     3 space 3 star
while i<=5:                           # --*****
    b=1                               # -*******
    while b<=5-i:                     # *********
        print(" ", end='')
        b=b+1
    j=1
    while j<=k:
        print("*", end='')
        j=j+1
    k=k+2
    print()
    i=i+1
print("------------")
#k is used to print the stars with the help of j also and b is for the space
#i is used to change the line


#   B   Printing number in Pyramid Shape
k=1                                   # ----1      
i=1                                   # ---333     
while i<=5:                           # --55555
    b=1                               # -7777777
    while b<=5-i:                     # 999999999
        print(" ", end='')
        b=b+1
    j=1
    while j<=k:
        print(k, end='')
        j=j+1
    k=k+2
    print()
    i=i+1
print("------------")


#    C    Printing number in Pyramid Shape
k=1                                   # ----1      
i=1                                   # ---123     
while i<=5:                           # --12345
    b=1                               # -1234567
    while b<=5-i:                     # 123456789
        print(" ", end='')
        b=b+1
    j=1
    while j<=k:
        print(j, end='')
        j=j+1
    k=k+2
    print()
    i=i+1
print("------------")


#   D     Printing number in Pyramid Shape
k=1                                   # ----1      
i=1                                   # ---222     
while i<=5:                           # --33333
    b=1                               # -4444444
    while b<=5-i:                     # 555555555
        print(" ", end='')
        b=b+1
    j=1
    while j<=k:
        print(i, end='')
        j=j+1
    k=k+2
    print()
    i=i+1
print("------------")


