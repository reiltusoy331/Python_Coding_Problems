
product = {"name":"shoes",
           "price": 100.00
           }


def create_sales_calc(rate):
    def sales_price_percent(p):
        return p['price'] - (rate * p["price"])    
    return sales_price_percent


new_price = create_sales_calc(.15)
print(new_price(product))