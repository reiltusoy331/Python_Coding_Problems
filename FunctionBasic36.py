def divide(x,y):
    return x // y

def second_arg_isnt_zero(func):
    def safe_version(x,y):
        if y == 0:
            print("Warning: The second argument value is zero.")
            return
        return func(x,y) 
    return safe_version

divide_safe = second_arg_isnt_zero(divide)     

print(divide_safe(10,0))