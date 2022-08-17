''' fibonacci series=0 1 1 2 3 5 8
fibonacci series using functions'''
while True:
    def fibonacci(n):
        a=0
        b=1
        if n==1:
            print(a)
        elif n<1:
            print("please enter positive number")
        else:
            print(a)
            print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
    num=int(input("enter the number of terms you want:"))
    fibonacci(num)









# a=0
# b=1
# n=int(input("enter a positive number:"))
# print(a)
# print(b)
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(c)





































