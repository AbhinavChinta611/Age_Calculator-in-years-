from datetime import date as d
  
def calculateAge(birthDate): 
    today = d.today() 
    age = today.year - birthDate.year-((today.month, today.day) < 
         (birthDate.month, birthDate.day)) 
  
    return age 

da = int(input("Enter Date : "))
mon = int(input("Enter Month : "))
y = int(input("Enter Year : "))
print(calculateAge(d(y, mon, da)), "years")
