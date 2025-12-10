#  A     Printing Stars '*' in Right Angle Triangle Shape using for loop
for i in range (1,6):                  # * 
    for j in range (1,i+1):            # * *
        print("*",end=' ')             # * * *     space or no space both works
    print()                            # * * * *
print("------------")


#  B    Printing number in Right Angle Triangle Shape using for loop
n=int(input("enter the number of rows="))
for i in range (1,n+1):                  # 1 
    for j in range (1,i+1):              # 1 2
        print(j,end=' ')                 # 1 2 3     space or no space both works
    print()                              # 1 2 3 4
print("------------")


#   C    Printing number in Right Angle Triangle Shape using for loop
n=int(input("enter the number of rows="))
for i in range (1,n+1):                  # 1 
    for j in range (1,i+1):              # 2 2
        print(i,end=' ')                 # 3 3 3     space or no space both works
    print()                              # 4 4 4 4
print("------------")


#  D     Printing number in Right Angle Triangle Shape using for loop
n=int(input("enter the number of rows="))     # *
for i in range (1,n+1):                       # * * 
    for j in range (1,i+1):                   # * * *
        print("*",end=' ')                    # * * * *     
    print()                                   # * * * * *
print("------------")


#    A   Printing Stars '*' in reverse Right Angle Triangle Shape
for i in range (1,6):                    #     *
    for b in range (1,6-i):              #    **
        print(" ",end='')                #   ***
    for j in range (1, i+1):             #  ****
        print("*",end='')                # *****     no space in end
    print ()
print("------------")


#    B   Printing number in reverse Right Angle Triangle Shape
n=int(input("enter the number of rows="))
for i in range (1,n+1):                    #     1
    for b in range (1,n+1-i):              #    22
        print(" ",end='')                  #   333
    for j in range (1, i+1):               #  4444
        print(i,end='')                    # 55555     no space in end
    print ()
print("------------")


#    C   Printing number in reverse Right Angle Triangle Shape
n=int(input("enter the number of rows="))
for i in range (1,n+1):                    #     1
    for b in range (1,n+1-i):              #    12
        print(" ",end='')                  #   123
    for j in range (1, i+1):               #  1234
        print(j,end='')                    # 12345     no space in end
    print ()
print("------------")


#    D   Printing Stars '*' in reverse Right Angle Triangle Shape
n=int(input("enter the number of rows="))
for i in range (1,n+1):                    #     *
    for b in range (1,n+1-i):              #    **
        print(" ",end='')                  #   ***
    for j in range (1, i+1):               #  ****
        print("*",end='')                  # *****     no space in end
    print ()
print("------------")


#    A  Printing Stars '*' in Pyramid Shape
k=1                                   # ----*      4 space and 1 star
for i in range (1,6):                 # ---***     3 space 3 star
    for b in range (1,6-i):           # --*****
        print(" ", end='')            # -*******
    for j in range (1, k+1):          # *********
        print("*", end='')
    k=k+2
    print()
print("------------")


#    B  Printing Stars '*' in Pyramid Shape
n=int(input("enter the number of rows="))
k=1                                   # ----*      4 space and 1 star
for i in range (1,n+1):               # ---***     3 space 3 star
    for b in range (1,n+1-i):         # --*****
        print(" ", end='')            # -*******
    for j in range (1, k+1):          # *********
        print("*", end='')
    k=k+2
    print()
print("------------")


#   C    Printing number in Pyramid Shape
n=int(input("enter the number of rows="))
k=1                                   # ----1
for i in range (1,n+1):               # ---333
    for b in range (1,n+1-i):         # --55555
        print(" ", end='')            # -7777777
    for j in range (1, k+1):          # 999999999
        print(k, end='')
    k=k+2
    print()
print("------------")


#   D    Printing number in Pyramid Shape
n=int(input("enter the number of rows="))
k=1                                   # ----1
for i in range (1,n+1):               # ---123
    for b in range (1,n+1-i):         # --12345
        print(" ", end='')            # -1234567
    for j in range (1, k+1):          # 123456789
        print(j, end='')
    k=k+2
    print()
print("------------")


#   E    Printing number in Pyramid Shape
n=int(input("enter the number of rows="))
k=1                                   # ----1
for i in range (1,n+1):               # ---222
    for b in range (1,n+1-i):         # --33333
        print(" ", end='')            # -4444444
    for j in range (1, k+1):          # 555555555
        print(i, end='')
    k=k+2
    print()
print("------------")


#    A   Printing star in inverted Right Angle Triangle Shape
for i in range(1,6):                        # *****
    for b in range(1,7-i):                  # ****
        print("*",end='')                   # ***     no space in end
    for j in range (1,i+1):                 # **
        print(" ",end='')                   # *     no space in end
    print ( )
print("------------")


#    B   Printing star in inverted Right Angle Triangle Shape
n=int(input("enter the number of rows="))
for i in range(1,n+1):                        # *****
    for b in range(1,n+2-i):                  # ****
        print("*",end='')                     # ***     no space in end
    for j in range (1,i+1):                   # **
        print(" ",end='')                     # *     no space in end
    print ( )
print("------------")


#    C   Printing number in inverted Right Angle Triangle Shape
n=int(input("enter the number of rows="))
for i in range(1,n+1):                        # 12345
    for b in range(1,n+2-i):                  # 1234
        print(b,end='')                       # 123     no space in end
    for j in range (1,i+1):                   # 12
        print(" ",end='')                     # 1     no space in end
    print ( )
print("------------")


#   D  Printing number in inverted Right Angle Triangle Shape
n=int(input("enter the number of rows="))
for i in range(1,n+1):                        # 11111
    for b in range(1,n+2-i):                  # 2222
        print(i,end='')                       # 333     no space in end
    for j in range (1,i+1):                   # 44
        print(" ",end='')                     # 5     no space in end
    print ( )
print("------------")


#  E  Printing star in inverted Right Angle Triangle Shape
n=int(input("enter the number of rows="))     # 666666
for i in range(1,n+1):                        # 11111
    for b in range(1,n+2-i):                  # 2222
        print(j,end='')                       # 333     no space in end
    for j in range (1,i+1):                   # 44
        print(" ",end='')                     # 5     no space in end
    print ( )
print("------------")


#   A    Printing Stars '*' in Opposite Pyramid Shape (METHOD 1)
n=int(input("enter the number of rows="))          # *********   for n=5
for i in range(n,0,-1):                            # -*******
    for b in range(1,n+1-i):                       # --*****
        print (" ",end='')                         # ---***
    for j in range (i,(i*2)-1):                    # ----*
        print ("*", end='')
    for j in range(1,i+1):
        print ("*", end="")
    print()
print("------------")


#    B    Printing Stars '*' in Opposite Pyramid Shape (METHOD 2)
rows = int(input("Enter number of rows= "))         #  * * * * * * * * * n=6
for i in range(rows, 1, -1):                        # - * * * * * * *
    for space in range(0, rows-i):                  # - - * * * * *
        print("  ", end="")                         # - - - * * *
    for j in range(i, 2*i-1):                       # - - - - *
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()
print("------------")


#   C    Printing number in Opposite Pyramid Shape
n=int(input("enter the number of rows="))          # 555555555  for n=5
for i in range(n,0,-1):                            # -4444444
    for b in range(1,n+1-i):                       # --33333
        print (" ",end='')                         # ---222
    for j in range (i,(i*2)-1):                    # ----1
        print (i, end='')
    for j in range(1,i+1):
        print (i, end="")
    print()
print("------------")


#   D    Printing number in Opposite Pyramid Shape
n=int(input("enter the number of rows="))          # 567812345   for n=5
for i in range(n,0,-1):                            # -4561234
    for b in range(1,n+1-i):                       # --34123
        print (" ",end='')                         # ---212
    for j in range (i,(i*2)-1):                    # ----1
        print (j, end='')
    for j in range(1,i+1):
        print (j, end="")
    print()
print("------------")


#   E    Printing number in Opposite Pyramid Shape
n=int(input("enter the number of rows="))          # 5555555555   for n=5
for i in range(n,0,-1):                            # -55555555
    for b in range(0,n+1-i):                       # --55555
        print (" ",end='')                         # ---555
    for j in range (i,(i*2)-1):                    # ----5
        print (n, end='')
    for j in range(1, i+1):
        print (n, end="")
    print()
print("------------")

