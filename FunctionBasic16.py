#Decorator basics

def my_first_function(func):
    def my_second_function():
        print("Beginning to execute the function!")
        func()
        print("The function has finished executing.")
    return my_second_function

def greeting():
    print("Hello, my name is John Doe, nice to meet you!")


my_decorator_func = my_first_function(greeting)

my_decorator_func()

