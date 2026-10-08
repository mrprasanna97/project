import csv
expense=[]
def add_expense(amount,category,date,note):
     person_expense={
          "AMOUNT":amount,
          "CATEGORY":category,
          "DATE":date,
          "NOTE":note
     }
     expense.append(person_expense)
     save_expense()
     print("EXPENSES ADDED")

def view_expense(expense):
      
      for i in expense:
          
          print("DATE :",i["DATE"]," | ","CATEGORY :",i["CATEGORY"]," | ","AMOUNT :","$",i["AMOUNT"]," | ","NOTE :",i["NOTE"])
def delete_expense():
    for idx,j in enumerate(expense):
        print(idx+1,"DATE :",j["DATE"]," | ","CATEGORY :",j["CATEGORY"]," | ","DATE :",j["DATE"]," | ","NOTE :",j["NOTE"])
    num=int(input("ENTER THE NUMBER TO DELETE :"))

    if num>=1 and num<=len(expense):
        removed=expense.pop(num-1)
        save_expense()
        print("DELETED :",removed["CATEGORY"],"-","$",removed["AMOUNT"])
def summary():
    print("\n----------SUMMARY----------")
    sum=0
    for i in expense:
     sum=sum+int(i["AMOUNT"])
    print("TOTAL SPENT : $",sum)
    print("------------------------\n")
def save_expense():
    with open("expenses.csv","w",newline="")as f:
        writer=csv.DictWriter(f,fieldnames=["AMOUNT","CATEGORY","DATE","NOTE"])
        writer.writeheader()
        writer.writerows(expense)

def load_expense():
    with open("expenses.csv","r")as f:
        reader=csv.DictReader(f)
        for row in reader:
           
           expense.append(row)
def main():
    while True:
     print("=======EXPENSE TRACKER=======")
     print("\n1.ADD EXPENSE")
     print("2.VIEW EXPENSES")
     print("3.SUMMARY")
     print("4 DELETE EXPENSES")
     print("5.EXIT\n")
     print("______________________________________")
     a=int(input("CHOOSE A NUMBER :"))
   
     if a==2:
          
          view_expense(expense)
          
     elif a==4:
         delete_expense()    
          
     elif a==5:
          print("\n ======EXIT=======")
          return
     elif a==1:
      
          amount=int(input("ENTER AMOUNT :"))
          category=input("ENTER CATEGORY :")
          date=input("ENTER DATE :")
          note=input("ENTER NOTES :")
          add_expense(amount,category,date,note)
      
     elif a==3:
         summary()
  

main()

          