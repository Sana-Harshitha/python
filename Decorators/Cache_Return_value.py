#Implement a decorator that caches the return values of a function ,so that when its called with same arguments, the cached value is returned insted of re-executinf the function\
import time
def cache(func):
    cache_value={}
    def wrapper(*args):
        print(f"Current cache: {cache_value}") 
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper
        
@cache
def long_running_functions(a,b):
    time.sleep(2)
    return a+b


print(long_running_functions(2,4))
print(long_running_functions(2,5))
print(long_running_functions(2,4))