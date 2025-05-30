def print_kwargs(**kwargs):
    print(kwargs)
    print(kwargs.items())
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    print("\n")


print_kwargs(name="IronMan",power="Suit",enemy="thanos")
print_kwargs(name="IronMan",power="Suit")
print_kwargs(name="IronMan")