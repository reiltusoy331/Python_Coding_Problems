def add(x,y):
    return x + y


def lists_to_dict(list1,list2):
    if len(list1) != len(list2):
        print('Lists must be the same length!!')
        return {}
    
    result_dict = {}

    for i in range(len(list1)):
        result_dict[list1[i]] = list2[i]

    return result_dict

print(lists_to_dict(['a','b','c'],[1,2,3,4]))