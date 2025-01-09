# partial application

def add(x,y,z):
    return x + y + z


def add_partial(x):
    def add_partial_inner(y,z):
        return add(x,y,z)
    
    return add_partial_inner

add10 = add_partial(10)

print(add10(20,30))