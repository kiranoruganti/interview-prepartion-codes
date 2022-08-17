'''0!=1 and also 1!=1'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))

# num=int(input("enter a number:"))
# print(factorial(num))


'''
5*
factorial(5-1)
factorial(4)
5*4*
factorial(3)
5*4*3*
factorial(2)
5*4*3*2*
factorial(2-1)
factorial(1)
5*4*3*2*1
'''



'''
n=4
n*factorial(n-1)=4*
factorial(n-1) anud thone factorial(3) aithadi so function malla call aithadi becuz of recursion

now in factorial(n) n becomes 3 becuz n-1
n=3
n*factorial(n-1)=4*3*

now in factorial(n) n becomes 2 becuz n-1
n=2
n*factorial(n-1)= 4*3*2*

now in factorial(n) n becomes 1 becuz n-1
n=1
if n==0 or n==1 becomes true and returns 1 this will be added to 4*3*2*1


'''