from functools import partial

person = {
    "Name":"Shaun",
    "Age":100
}

job_listing = {"Name":"Python Developer"}

buildings = {"Name":"Eiffel Tower"}

def get_entry(dict,key,default_value):
    if key in dict:
        return dict[key]
    else:
        return default_value
    
def get_entry_partial(key,default_value):
    def inner(dict):
        return get_entry(dict,key,default_value)
    return inner

get_name = partial(get_entry, key="Name")
get_name_un = partial(get_entry, key="Name",default_value="Unknown")

print(get_name(person,default_value="Unknown")) 
print(get_name_un(job_listing)) 

 

 