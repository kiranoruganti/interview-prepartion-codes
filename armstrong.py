'''
153=1 cube+3cube +5cube=1+27+125=153
'''

arm=int(input("enter a number:"))#153

temp=arm
sum=0
while(arm>0):
    r=arm%10                   #remainder3
    sum=sum+r**3
    arm=arm//10                 #quotient 15
    # print(sum)


if temp==sum:
    print("armstrong number")
else:
    print("not a arm strong number")

