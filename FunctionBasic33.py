person = {
    "Name":"Shaun",
    "Age":100
}

def get_entry(dict,key,default_value):
    if key in dict:
        return dict[key]
    else:
        return default_value
    
def get_entry_partial(key,default_value):
    def inner(dict):
        return get_entry(dict,key,default_value)
    return inner

get_name = get_entry_partial("Name","N/A")

print(get_name(person))


