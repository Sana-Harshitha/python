n= int(input("enter a number: "))
sum_of_even =0
for i in range (1,n+1):
    if(i%2==0):
        sum_of_even+=i
print(f"Even Number sum upto {n} is {sum_of_even}")