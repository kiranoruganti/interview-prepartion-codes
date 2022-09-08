# Fibonacci series using recursion
def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)


n=5
for i in range(n):
	print(fibonacci(i))


# fib(0)=0
# fib(1)=1
#
# n=2
# fib(2)
# fib(n-1)+fib(n-2)
# fib(1)+fib(0)
# 1+0
#
# fib(2)=1
#
# n=3
# fib(3)
# fib(n-1)+fib(n-2)
# fib(2)+fib(1)
#
# 1+1=2
# fib(3)=2
#
# n=4
# fib(4)
# fib(n-1)+fib(n-2)
# fib(3)+fib(2)
# 2+1=3
# fib(4)=3








# if __name__ == "__main__":
# 	n = 9
# 	print(fibonacci(n))


