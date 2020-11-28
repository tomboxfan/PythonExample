'''
Requirement:
1) implement NTUC supermarket price calculator

2) Customer can buy - beef / pork / tomato / apple / orange

3) beef / pork / tomato - total price calculated by weight
   beef - $20 / kg
   pork - $16 / kg
   tomato - $5 / kg

4) apple / orange - total price calculated by quantity
   apple - $5 for 5 apples; $1.6 each
   orange - $5 for 3 orange; $2 each
'''

welcome_msg = '''
***********************************
    Welcome to NTUC Supermarket
***********************************
'''

print(welcome_msg)

product_prices = '''
----------------------------
beef   - $20 / kg
pork   - $16 / kg
tomato - $5 / kg
apple  - $5 for 5 apples; $1.6 each
orange - $5 for 3 orange; $2 each   
----------------------------
'''
print(product_prices)

product_name = input("What product do you want to buy (beef / pork / tomato / apple / orange): ")

total_price = 0

if product_name == 'beef' or product_name == 'pork' or product_name == 'tomato':
    total_weight = float(input("Total weight(kg): "))

    if product_name == 'beef':
        unit_price = 20 # $20 / kg
    elif product_name == 'pork':
        unit_price = 16 # $16 / kg
    else:
        unit_price = 5

    total_price = unit_price * total_weight
    print(f'{product_name} : ${unit_price} * {total_weight} = ${total_price}')

elif product_name == 'apple' or product_name == 'orange':
    pass

else:
    print(f'Unrecognized product : {product_name}')

