# custom partial application function currying

def add(x,y,z):
    return x+y+z

def add_partial(x):
    def inner1(y):
        def inner2(z):
            return add(x,y,z)
        return inner2
    return inner1


add10 = add_partial(10)
add10and20 = add10(20)

print(add10and20(30))
