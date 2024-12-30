# First Class Function
# Passing define function as an argument to other functions


def log_string(string, format):
    print(format(string))

def uppercase_string(string):
    return string.upper()


log_string("hello", uppercase_string)



