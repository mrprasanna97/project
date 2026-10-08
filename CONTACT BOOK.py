contact=[]
def add_contact(name,phno):
    a={
        "name":name,
        "phone":phno
     }
    contact.append(a)
    print("CONTACT ADDED")
def view_contact():
    if not contact:
        print("NO CONTACT")
    for i in contact:
        print("NAME :",i["name"].upper(),"|","PHONE NUMBER :",i["phone"])
def search_contact(names):
    for i in contact:
        if names==i["name"]:
          print("NAME :",i["name"].upper(),"|","PHONE NUMBER :",i["phone"])  
def delete_contact():
    
    for idx,i in enumerate(contact):
        print(idx+1,"NAME :",i["name"].upper(),"|","PHONE NUMBER :",i["phone"]) 
    num=int(input("ENTER THE NUMBER :"))
    contact.pop(num-1)
    print("CONTACT DELETED")  
 
def main():
  while True:
    print("____________________________________")
    print("\n1. ADD CONTACT")
    print("2. VIEW CONTACT")
    print("3. SEARCH CONTACT")
    print("4. DELETE CONTACT")
    print("5. EXIT")
    print("____________________________________")
    c=int(input("CHOOSE THE NUMBER :"))
    if c==1:
        name=input("ENTER NAME :")
        phno=int(input("ENTER NUMBER :"))  
        add_contact(name,phno)    
    elif c==2:
        view_contact()
    elif c==3:
        names=input("ENTER NAME :")
        search_contact(names)
    elif c==4:

        delete_contact() 
    elif c==5:
        return
    
        
main()