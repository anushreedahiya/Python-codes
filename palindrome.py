#example "wow"
def is_palindrome(s):
    return s==s[::-1]
    
#driver code
s=input("enter a string=")
a=is_palindrome(s)
if a:
    print("yes")
else:
    print("no")


#right
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")