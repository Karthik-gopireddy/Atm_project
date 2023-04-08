import time
import datetime
print("****WELCOME TO ATM****")
print("------------------------------")
pin=9966
amount=50000
while(True):
    a=int(input("ENTER YOUR ATM PIN : "))
    if(a==pin):
        print('''1.withdrawl money
                 2.mini statement
                 3.deposit money
                 4.exit''')
        while(True):
            b=int(input("ENTER YOUR CHOICE : "))
            if(b==1):
                withd=int(input("ENTER THE AMOUNT TO WITHDRAWL : "))
                amount=amount-withd
                print("transaction is sucessfull")
                print("withdrawl amount is :",withd)
                n2000=withd/2000
                n500=(withd/2000)%500
                n200=(withd/500)%200
                print("%d",n2000)
                print("%d",n500)
                print("%d",n200)

            elif(b==2):
                print("*******WELCOME TO ATM********")
                print("------------------------------")
                a=datetime.datetime.now()
                print(a.strftime("%c"))
                print("your current balance is : ",amount)
            elif(b==3):
                a=int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT : "))
                amount+=a
                print("your deposit amount is : ",a)
                print("deposit is sucessfull")
                print("your current balance is : ",amount)
            elif(b==4):
                exit()
            else:
                print("IN-VALID CHOICE PLEASE")
            
            

    else:
        print("ENTER THE VALID PIN")

