
def add(a, b):
    return a + b

def partial_add(a):
   
    def inner(b):
        return add(a, b)
    return inner


add_10 = partial_add(10)


result = add_10(5)

print(result)  
