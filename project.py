import datetime
print("__________________________________________________________________")
print("TEA - 1")
print("COFFEE - 2")
print("BISCUT -3")
print("EGG PUFFS -4")
print("JUICE - 5")
print("__________________________________________________________________")
class product:
    def __init__(self):
       self.pname=""
       self.amount=""
       self.product=""

    def dis(self):
       if self.pname==1:
          self.quantity=int(input("ENTER TEA QUANTITY :"))
          self.amount=10*self.quantity
          self.product="TEA    "
       elif self.pname==2:
           self.quantity=int(input("ENTER COFFEE QUANTITY :"))
           self.amount= 20*self.quantity
           self.product="COFFEE"
       elif self.pname==3:
          self.quantity=int(input("ENTER BISCUTS QUANTITY :"))
          self.amount= 10*self.quantity
          self.product="BISCUT"
       elif self.pname==4:
          self.quantity=int(input("ENTER EGG PUFFS QUANTITY :"))
          self.amount= 20*self.quantity
          self.product="EGG PUFFS"
       elif self.pname==5:
           self.quantity=int(input("ENTER JUICE QUANTITY :"))
           self.amount=10*self.quantity
           self.product="JUCIE"
       else:
           self.quantity=0
           self.amount=0
           self.product="NOTHING"
    def line(self):
        print("__________________________________________________________________")
    def display(self):         
        
         print("   ",self.pname,"\t\t ",self.product,"\t",self.quantity,"    ",self.amount)
         



n1=product()
n2=product()
n3=product()
n1.pname=int(input("NO :"))
n2.pname=int(input("NO :"))
n3.pname=int(input("NO :"))
print("__________________________________________________________________")


n1.dis()
n2.dis()
n3.dis()
n1.line()

print("DATE :",datetime.date.today())
a=datetime.datetime.now()
print("TIME :",a.strftime("%H.%M.%S"))
print("__________________________________________________________________")

print("PRODUCT NO \tPRODUCT NAME \t QTY \tAMOUNT")
n1.display()
n2.display()
n3.display()

total=(n1.amount + n2.amount)+n3.amount
print("__________________________________________________________________")
print("\nTOTAL :",total)
print("__________________________________________________________________")
num=int(input("\nENTER A CASH :"))
print("\nREMAINING :",num-total)


print("\n\t.....THANK YOU VISIT AGAIN.....")