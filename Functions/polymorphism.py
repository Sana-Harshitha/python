def multiply(p1, p2):
    try:
        return p1 * p2
    except TypeError:
        return f"Invalid operation: Cannot multiply {p1} and {p2}."


print(multiply(8,5))
print(multiply('a',5))
print(multiply(5,'b'))
print(multiply('a','b'))