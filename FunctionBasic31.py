# custom partial application function example

def partial_apply(func, *args):
    def wrapper(*more_args):
        return func(*args, *more_args)
    return wrapper


def multiply(a, b, c):
    return a * b * c


multiply_by_2_and_3 = partial_apply(multiply, 2, 3)


result = multiply_by_2_and_3(4)  
print(result)  # Output: 24
