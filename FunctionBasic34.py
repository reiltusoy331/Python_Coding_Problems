from functools import partial

def add(w,x,y,z):
    return w+x+y+z


add10and20 = partial(add,30,40)

print(add10and20(10,20))