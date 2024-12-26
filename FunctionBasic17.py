def prettify(func):
    def wrapper():
        print("********************************************")
        func()
        print("********************************************")
    return wrapper


@prettify
def banner():
    print("AUTHORIZED PERSONNEL CAN ACCESS THIS DEVICE!")

banner()