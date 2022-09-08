n=int(input("enter a number:"))
if n<=0:
    print("please enter a positive number")
else:
    sum=0
    for i in range(1,n+1):
        sum=sum+i
        n=n-1
        print(sum)