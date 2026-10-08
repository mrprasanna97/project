import random

name=input("ENTER YOUR NAME :")
print("____________________________________________________________")
print("1 - easy(3 attempt, (1,10))")
print("2 - moderate(5 attempt, (1,50))")
print("3 - hard(10 attempt, (1,100))")
print("____________________________________________________________")
while True:
   num=input("SELECT 1,2,3 :")
   if(num=="1"):
      max_number,max_attempts=10,3
      break
   elif(num=="2"):
      max_number,max_attempts=50,5
      break
   else:
      max_number,max_attempts=100,10
      break
print("___________________________________________________________________________________________________")  
print("\nOKAY ",name.upper()," NOW YOU SELECT ",num,". YOU HAVE ",max_attempts,"ATTEMPTS"," AND THE NUMBER BETWEEN ",(1,max_number))
print("___________________________________________________________________________________________________")
guess=random.randint(1,max_number)
attempts=0
class g1:
   def __init__(self):
     if(num=="1"):
      self.guess=int(input("GUESS A NUMBER BETWEEN 1 AND 10 :"))
      
     elif(num=="2"):
       self.guess=int(input("GUESS A NUMBER BETWEEN 1 AND 50 :")) 
     elif(num=="3"):
        self.guess=int(input("GUESS A NUMBER BETWEEN 1 AND 100 :"))
   def display(self):
          
        if(guess>self.guess):
          print("TOO LOW")

        elif(guess<self.guess):
           print("TOO HIGH")

        elif(guess==self.guess):
           print("YOU ARE CORRECT")
           print("\nTHE GUESS NUMBER IS :",guess)
           exit()
     
       
if(num=="1"):
 n1=g1()
 n1.display()
 n2=g1()
 n2.display()
 n3=g1()
 n3.display()

elif(num=="2"):
   n1=g1()
   n1.display()
   n2=g1()
   n2.display()
   n3=g1()
   n3.display()
   n4=g1()
   n4.display()
   n5=g1()
   n5.display()
else:
   n1=g1()
   n1.display()
   n2=g1()
   n2.display()
   n3=g1()
   n3.display()
   n4=g1()
   n4.display()
   n5=g1()
   n5.display()
   n6=g1()
   n6.display()
   n7=g1()
   n7.display()
   n8=g1()
   n8.display()
   n9=g1()
   n9.display()
   n10=g1()
   n10.display()
print("\nTHE GUESS NUMBER IS :",guess)



