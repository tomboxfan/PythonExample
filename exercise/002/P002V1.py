x = input("Show me the money:") # get str userInputStr
profit = int(x) # convert str userInputStr to int  using int constructor

bonus = float() # decimal 0.1, 0.4


if profit < 100000:
    bonus = profit * 0.1


# elif -> 如果不是 profit < 100000 , 而是 profit <= 200000
elif profit <= 200000:
    bonus = 100000 * 0.1                # = : assign value. assign a value to a variable
    bonus += (profit - 100000) * 0.075 # += : bonus += x -> bonus = bonus + x

# elif -> 如果不是 profit < 100000 , 而是 profit <= 200000
elif profit <= 400000:
    bonus = 100000 * 0.1
    bonus += 100000 * 0.075
    bonus += (profit - 200000) * 0.05

elif profit <= 600000:
    bonus = 100000 * 0.1
    bonus += 100000 * 0.075
    bonus += 200000 * 0.05
    bonus += (profit - 400000) * 0.03

elif profit <= 1000000:
    bonus = 100000 * 0.1
    bonus += 100000 * 0.075
    bonus += 200000 * 0.05
    bonus += 200000 * 0.03
    bonus += (profit - 600000) * 0.015

else:
    bonus = 100000 * 0.1
    bonus += 100000 * 0.075
    bonus += 200000 * 0.05
    bonus += 200000 * 0.03
    bonus += 400000 * 0.015
    bonus += (profit - 1000000) * 0.01





print("The bonus is:", bonus)