# Tuple unpacking via python custom function

def user_info():
    name = "John Doe"
    age = 32
    location = "Renton, WA"
    return name,age,location

name, age, location = user_info()


print("Name: ",name)
print("Age: ",age)
print("Location: ",location)



