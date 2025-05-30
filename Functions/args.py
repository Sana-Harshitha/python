def  sum_all(*args):
    print(args)  #tuple
    print(*args)
    return sum(args)

print(sum_all(1,2,3))