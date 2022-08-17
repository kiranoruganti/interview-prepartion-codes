'''
num=787
temp=num
sum=0
r=num%10=787%10=7
num=num//10=787//10=78


'''


num=int(input("enter a number:"))
temp=num
sum=0
while (num>0):
    r=num%10
    sum=sum*10+r
    num=num//10
#print(sum)

if temp==sum:
    print(temp,"palindrome number")
else:
    print(temp,"not a palindrome")






