import random
c=["ROCK","PAPER","SCISSORS"]
a=random.choice(c)
def main():
 while True:
  print("==========YOU ARE GOING TO PLAY WITH COMPUTER===========")

  print("\n•ROCK ")
  print("•PAPER")
  print("•SCISSORS")
  
  choice=input("\nPICK THE ONE :")
  b=choice.upper()
  if b==a:
    print("YOU ARE CORRECT 👍",a)
  else:
    print("YOU ARE WRONG 👎",a)
  P=int(input("TO CONTINUE PRESS 1 :"))
  if P==1:
    main()
  else:
    print("INVALID NUMBER")
main()
