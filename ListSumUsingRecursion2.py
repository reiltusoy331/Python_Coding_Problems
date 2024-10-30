mylist = [4,5,6]

def find_sum(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + find_sum(s[1:])
    


print(find_sum(mylist))
print(mylist[1:])
