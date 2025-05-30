num = int (input("enter a number: "))

for i in range (1,11):
   if i == 5:
      continue
   print(num,"X", i , '=', num * i)