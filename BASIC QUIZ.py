
A={
    "WHAT IS CAPITAL OF INDIA :":"DELHI",
    "WHAT IS 5+2 :":"7",
    "FULL FORM OF SBI :":"STATE BANK OF INDIA"

}
score=0
for i in A:
 print(i,end="")
 c=input()
 if c.upper()==A[i]:
  score=score+1
print(score)
