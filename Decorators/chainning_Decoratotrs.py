def add_greeting(func):
    def wrapper(name):
        return f"Hello, {func(name)}!"
    return wrapper

def make_uppercase(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

@add_greeting
@make_uppercase
def get_name(name):
    return name

print(get_name("Alice"))
