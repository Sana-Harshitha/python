# $12 for adults(18 and over) $8 for children .Everyone gets a $2 disscount on Wednessday
age=int(input("Enter Your Age: "))
day=input("Enter the Week Day: ")

price =12 if age>= 18 else 8
if day=="Wednesday":
  price -=2
print("Your Price is ",price)  