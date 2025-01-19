# from list to dictionary with error checking wrapper

def args_same_length(func):
    def safe_version(*args,**kwargs):
        if len(args[0]) != len(args[1]):
            print("Warning! The length of both lists dont match.")
            return 
        return func(*args,**kwargs)
    return safe_version


def list_to_dict(l1,l2):

    dict = {}
    for index,key in enumerate(l1):
        dict[key] = l2[index]

    return dict

list_to_dist_pluscheck = args_same_length(list_to_dict)

print(list_to_dist_pluscheck(['a','b','c'],[1,2,3]))
