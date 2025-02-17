#nested loop snippet code 
i=1;
while i<5:
    j=1;
    while j<5:
        print (j);
        j=j+1;
    i=i+1;
print("------------")


#Printing Stars '*' in Right Angle Triangle Shape
i=1;                                   # *
while i<=5:                            # * *
    j=1;                               # * * *
    while j<=i:                        # * * * *
        print("*",end=' ')             # * * * * *     space or no space both works
        j=j+1;
    print ()
    i=i+1
print("------------")


#printing number in right angle triangle shape
i=1;                                     # 1
while i<=5:                              # 2 2
    j=1;                                 # 3 3 3
    while j<=i:                          # 4 4 4 4
        print(i,end=' ')                 # 5 5 5 5 5
        j=j+1;
    print ()
    i=i+1
print("------------")
    

#printing number in right angle triangle shape
i=1;                                     # 1
while i<=5:                              # 1 2
    j=1                                  # 1 2 3
    while j<=i:                          # 1 2 3 4
        print(j,end=' ')                 # 1 2 3 4 5
        j=j+1;
    print ()
    i=i+1
print("------------")


#Printing Stars '*' in reverse Right Angle Triangle Shape
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


#Printing Stars '*' in Triangle Shape
i=1;                                     #      *
while i<=5:                              #     * *
    b=1;                                 #    * * *
    while b<=5-i:                        #   * * * *
        print(" ",end='')                #  * * * * * 
        b=b+1;
    j=1
    while j<=i:
        print("*",end=' ') #space is end gives us this output
        j=j+1
    print ()
    i=i+1
print("------------")


#Printing Stars '*' in Right Angle Triangle Shape
i=1;                                     #         *
while i<=5:                              #       **
    b=1;                                 #     ***
    while b<=5-i:                        #   ****
        print(" ",end=' ')               # *****      space in end for this pattern
        b=b+1;
    j=1
    while j<=i:
        print("*",end='') #no space in the end
        j=j+1
    print ()
    i=i+1
print("------------")
  

    
