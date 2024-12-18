from functools import reduce


my_list_num =[0,1,2,3,4,5]

def addition(x,y):
    result = x+y
    return result


largest_num = reduce(lambda x,y: x if x > y else y, my_list_num)

print(largest_num) 