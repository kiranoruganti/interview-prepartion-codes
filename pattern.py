# print("*")
# print("**")
# print("****")
# print("*****")
# print("******")


# print("*",end=" ")
# print("**",end="")
# n=int(input("how many rows do you want"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


rows = int(input("Enter number of rows: "))

k = 0

for i in range(rows):
    for space in range((rows - i) ):
        print(end="  ")

    while k != (2 * i - 1):
        print("* ", end="")
        k += 1

    k = 0
    print()
