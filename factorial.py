num=int(input("enter a number:"))
fact=1

if num<0: #NEGATIVE NUMBERS DOESNOT HAVE A FACTORIAL
    print("please enter a positive number")
elif num==0:
    print(fact)
else:
    for i in range(1,num+1):
        fact= fact * i
    print(f"the factorial of {num} is {fact}")
