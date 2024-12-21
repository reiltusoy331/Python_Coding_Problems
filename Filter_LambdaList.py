prod_items = [("Product1",15.59),("Product2",12.59),("Product3",5.75)]


filtered = list(filter(lambda item: item[1] > 10, prod_items))

print(filtered)