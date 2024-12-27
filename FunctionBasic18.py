# Decorator Passing arguments

def politeness(func):
    def wrapper(name):
        print("Thank you for reacting to this video!")
        func(name)
        print("Dont forget to share and hit the subscribe button!")
    return wrapper


@politeness
def subscriber(name):
    print(f"Hi {name}")

subscriber("Gello")
