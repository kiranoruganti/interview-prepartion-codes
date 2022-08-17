'''
if a number is divisible by one and itself is called a prime number
take a number
when the taken number is divisible by one and itself is called a prime number
otherwise it is not prime number
1 is not a prime number
'''








num =int(input("enter a number:"))

# If given number is greater than 1(1 thoni divide aithadi kabatti no need to check 1 check greater than 1 numbers)

if num > 1:

    # Iterate from 2 to num
    for i in range(2, (num)):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break

    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
















































