#Lambda function

# example 1

add = lambda x, y:  x + y
log = lambda statement: print(statement)

print(add(1,2))
log("Hello World")



# example 2

numbers = [1,2,3]
new_value = list(map(lambda x: x*2,numbers))
print(new_value)