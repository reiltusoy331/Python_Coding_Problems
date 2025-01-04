# higher order function

def print_wrap(func):
    def func_enhanced(*args,**kwargs):
        print("Function was called with args:")
        print(args)
        print(kwargs)

        result = func(*args, **kwargs)
        print(f"The result is: {result}")
        
        return result

    return func_enhanced


def add_3(x,y,z):
    return x+y+z


add_3_enhanced = print_wrap(add_3)

sum = add_3_enhanced(10,20,30)

print(f"The sum is: {sum}")