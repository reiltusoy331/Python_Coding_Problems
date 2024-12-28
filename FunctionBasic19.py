# Generators

def square_me(list_of_nums):
    for num in list_of_nums:
        yield (num*num)

gen_obj = square_me([1,2,3,4,5])

for obj in gen_obj:
    print(obj)

