def get_value_with_default(dict, key,default_value):
    if key in dict:
        return dict[key]
    else:
        return default_value

def get_value_partial(key, default_value):
    def inner(dict):
        return get_value_with_default(dict, key,default_value)

    return inner


get_name = get_value_partial('name','Unknown')

#empty dict, expect Unknown string result
print(get_name({}))

print(get_name({'name':'Reil'}))