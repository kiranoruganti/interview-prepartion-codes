'''
1.give username
2.give password
if username and password are correct ask for cash withdrawal
if username and password are incorrect decline transaction
'''


username=input("enter username:")
password=input("enter password:")

abc=True
while abc:

    if username=="teja" and password=="teja123":
        cash=int(input("enter cash:"))
        print("transaction sucessfull")
        receipt=input("press 'y' if you want receipt and press 'n':")
        if receipt=="y":
            print(cash,"taken")
            abc=False
            break
        else:
          print("    ")
          abc=False
          break

    else:
        print("transaction unsuccessful due to wrong credentials")
        #abc=False
        break