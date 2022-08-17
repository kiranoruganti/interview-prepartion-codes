a=input("enter a string:")
print("a=",a)
b=a[::-1]
print("b=",b)

if a==b:
    print(a,"is a palindrome string")
else:
    print(a,"is not a palindrome string")