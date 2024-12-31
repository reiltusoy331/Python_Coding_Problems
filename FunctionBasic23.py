# First Class Function
# Return functions to other functions

def greetings():
    def say_hello():
        print("Hello from inner function.")
    return say_hello

mssg = greetings()
mssg()


