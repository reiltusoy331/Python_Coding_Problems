from inspect import signature

def get_number_of_args(func):
    return len(signature(func).parameters)


def get_value_with_default(key,default_value,dict,a,b,c):
    if key in dict:
        return dict[key]
    
    else:
        return default_value
    

print(get_number_of_args(get_value_with_default))