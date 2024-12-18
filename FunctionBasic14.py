mylist_num =[1,2,3,4,5]

def squared(num):
    return num **2

squared_numbers = map(squared,mylist_num)
print(list(squared_numbers))


lambda_cube_num = map(lambda x: x**3,mylist_num)
print(list(lambda_cube_num))
 