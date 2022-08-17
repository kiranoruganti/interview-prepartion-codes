a=29
b=20
print("Before Swapping a=",a,"b=",b)
temp=a
a=b
b=temp
print(a)
print(b)
print("After Swapping a=",a,"b=",b)



#without using third variable
a=29
b=20
print("Before Swapping a=",a,"b=",b)
a,b=b,a
print("After Swapping a=",a,"b=",b)