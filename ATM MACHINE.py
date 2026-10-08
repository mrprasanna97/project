balance=10000
password=720080
def dep(amount):
    global balance
    balance=balance+amount
    print("........DEPOSIT SUCCESSFULL.......")
def withdraw(p,a):
    global balance,password
    
    if p==password:
     balance=balance-a
     print(".........WITHDRAW SUCCESSFULL........")
    else:
       print("INVALID PIN")
def bal(pa):
    global balance,password
   
    if pa==password:
     print("YOUR BANK BALANCE :",balance)
def menu():
  while True:
   
    print("=============SBI BANK============")
    print("1.DEPOSIT")
    print("2.WITHDRAW")
    print("3.CHECK BALANCE")
    print("4.EXIT")
    print("__________________________________")
    num=int(input("ENTER NUMBER :"))
    if num==1:
        amount=int(input("ENTER A AMOUNT TO DEPOSIT :"))
        dep(amount)
    elif num==2:
         p=int(input("ENTER YOUR 6 DIGIT PIN :"))
         a=int(input("ENTER AMOUNT TO WITHDRAW :"))
         withdraw(p,a)
    elif num==3:
        pa=int(input("ENTER YOUR 6 DIGIT PIN :"))
        bal(pa)
    elif num==4:
        print("...EXIT...")
        return
menu()