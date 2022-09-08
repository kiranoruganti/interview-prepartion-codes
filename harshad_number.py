'''If a number is divisible by the sum of its digits, then it will be known as a Harshad Number.

For example:

The number 156 is divisible by the sum (12) of its digits (1, 5, 6 ).

Some Harshad numbers are 8, 54, 120, etc.
'''

num=int(input("enter a number:"))
rem=0
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10

if temp%sum==0:
    print(temp," is a harshad number")
else:
    print(temp,"not a harshad number")
