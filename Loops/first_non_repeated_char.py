input_string=input("enter a string: ")

for char in input_string:
    if input_string.count(char)==1:
        print("First Non Repeated Char is ", char)
        break