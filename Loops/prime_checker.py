num = int (input("Enter a number: "))
is_prime=True
if num>1:
    for i in range (2,num):
        if num % i ==0:
            is_prime=False
            break

print ("prime" if is_prime==True else "not a prime")