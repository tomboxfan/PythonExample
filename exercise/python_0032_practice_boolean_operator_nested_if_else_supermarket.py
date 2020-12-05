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

5) implement a membership system, member will get 10% discount
    i) you need to ask customer, "Are you a member?"
    ii) customer can answer 'y', 'Y', 'Yes', 'yes'. All 4 answers mean he is a NTUC member.

6) implement a payment system, which supports Visa/Mastercard/NETS/Cash
    i) If user pays with Visa/Mastercard, you need to ask user to sign his name. (Use input() to get user's signature)
    ii) If user pays with NETS, you need to ask user to input his card's password. (Use input() to get user's password)
    iii) If user pays with Cash, you need to check whether you should give customer some change, whether he has paid enough money.

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

product_name = ''
total_price_for_all_products = 0

while product_name != 'exit':

    product_name = input("What product do you want to buy (beef / pork / tomato / apple / orange / exit): ")

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

        # 1st step:
        total_count = int(input("Total quantity:"))

        if product_name == 'apple':
            # 2nd step:
            group_count = total_count // 5  # 取整
            single_count = total_count % 5  # 取余

            # 3rd step:
            group_price = 5
            single_price = 1.6
        else:
            # 2nd step:
            group_count = total_count // 3  # 取整
            single_count = total_count % 3  # 取余

            # 3rd step:
            group_price = 5
            single_price = 2

        group_price_total = group_count * group_price
        single_price_total = single_count * single_price
        total_price = group_price_total + single_price_total

        # 4th step
        print(f'{product_name} : ${total_price}')

    elif product_name == 'exit':
        break

    else:
        print(f'Unrecognized product : {product_name}')

    total_price_for_all_products += total_price


# membership -------------------------------------------------------
member_str = input("Are you a member? ")

if member_str == 'Y' or member_str == 'y' or member_str == 'Yes' or member_str == 'yes':
    total_price_for_all_products *= 0.9
    print(f'After discount, total price: ${total_price_for_all_products}')

# payment ----------------------------------------------------------

payment = input("Will you pay using Visa / Mastercard / NETS / Cash? ")

if payment == 'Visa' or payment == 'Mastercard':
    signature = input("Please sign your name: ")
    print(f'Signature {signature} is well received.')
    print(f'${total_price_for_all_products} has been charged to your {payment} card.')
elif payment == 'NETS':
    password = input("Please input your NETS card password: ")
    print(f'${total_price_for_all_products} has been charged to your NETS card.')
elif payment == 'Cash':
    total_paid = float(input("How much will you pay? "))

    if total_paid > total_price_for_all_products:
        print(f'Here comes your change: ${total_paid - total_price_for_all_products:.2f}')
    elif total_paid < total_price_for_all_products:
        print(f'You are still short of ${total_price_for_all_products - total_paid:.2f}. I am sorry, I cannot give your goods.')
    else:
        print(f"You've paid the exact amount.")

# bye bye ------------------------------------------------------------

bye_msg = '''
*********************
   See you again! 
*********************
'''
print(bye_msg)
