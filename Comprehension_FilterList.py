prod_items = [("Product1",15.59),("Product2",12.59),("Product3",5.75)]

filtered = [item for item in prod_items if item[1] > 10]

print(filtered)