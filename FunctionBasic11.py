# Comprehensions


interface_list = ["GigaEth0/1","GigaEth0/2","GigaEth0/3","Loopback0","Loopback1"]

# gigabit_list =[]
# for interface in interface_list:
#     if interface.startswith("GigaEth"):
#         gigabit_list.append(interface)


# Comprehensions Method

gigabit_list =[interface for interface in interface_list if interface.startswith("GigaEth")]

print(gigabit_list)

