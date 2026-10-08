
import csv
import json

with open("stu_data.csv","w")as f:
       writer=csv.writer(f)
       writer.writerow(["name","mark 1","mark 2","mark 3","mark 4","mark 5","mark 6"])
       writer.writerow(["prasanna",89,91,93,97,92,87])
       writer.writerow(["balamurugan",95,90,96,87,97,93])
       writer.writerow(["shankar",89,98,90,76,89,99])
def calculate_total(row):
    try:
       
       add=int(row["mark 1"])+int(row["mark 2"])+int(row["mark 3"])+int(row["mark 4"])+int(row["mark 5"])+int(row["mark 6"])
       return add
    except ValueError:
          print("INVALID MARK FOR :",row["name"])
def calculate_average(row):
         
            add=int(row["mark 1"])+int(row["mark 2"])+int(row["mark 3"])+int(row["mark 4"])+int(row["mark 5"])+int(row["mark 6"])
             
            return round(add/6,3) 
           
     
def get_grade(average):
             
              if average<35:
                 return "FAIL 👎"
              elif 35<average<50:
                  return "C 😒"
              elif 50<average<90:
                  return "B 👍"
              elif average>90:
                  return "A 👌"
              
           

result=[]
try:
 with open("stu_data.csv","r")as f:
     reader=csv.DictReader(f)
     for row in reader:
      try:
          sum=calculate_total(row)
          average=calculate_average(row)
          gra=get_grade(average)
          student_result={
                "NAME ":row["name"].upper(),
                "TOTAL ":sum,
                "AVERAGE ":average,
                "GRADE ":gra
                  }
          result.append(student_result)
      except ValueError:
                      print("INVALID MARK FOR :",row["name"]) 
      except KeyError:
               print("HEADER NAME IS MISSING.....") 
except FileNotFoundError:
                    print("'stu_data.csv' FILE IS NOT FOUND")
with open("report.json","w")as f:
      json.dump(result,f,indent=4)
with open("report.json","r")as f:
       b=json.load(f)
       print(b)
