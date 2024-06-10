#Create a list with menu items in it
#create 2 dictionaries: 1 with stock of items and another with price of items
# using for loop to work out the stock value of items using: item_value = (stock[items] * price[items])

menu = ["cake","tea","coffee","water"] # lists-items
#         key  : value
stock = {"cake":200, #dictionary-stock
       "tea"   :100,
       "coffee": 300,
       "water" : 20}

price = {"cake":4, #dictionary-price
       "tea"   :2,
       "coffee":3.50,
       "water" :1}
item_value = 0

for items in menu:
    item_value += stock[items] * price[items]
    print(item_value)

print("The total stock wroth in the cafe is $" , item_value)