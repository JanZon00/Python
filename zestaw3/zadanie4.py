import functools

def pamiec(func):
    memory = {}
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):

        if args in memory:
            return memory[args]
        else:
            val = func(*args)
            memory[args] = val
            return val
    return wrapper

@pamiec    
def fibonacci(n): 
        return n if 0 <= n < 2  else fibonacci(n - 1) + fibonacci(n - 2)
    
for i in range(100): 
    print(fibonacci(i))
        