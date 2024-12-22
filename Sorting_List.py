prod_items = [("Product1",15.59),("Product2",12.59),("Product3",5.75)]

def sorting_items(items):
    return items[1]


prod_items.sort(key=sorting_items)
print(prod_items)   