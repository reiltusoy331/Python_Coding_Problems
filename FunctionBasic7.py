def print_my_args(**kwargs):
    for key,value in kwargs.items():
        print(f"The argument {key} was passed into this function with a value of {value}")

print_my_args(name='john',job='python developer',hobbies='jogging')