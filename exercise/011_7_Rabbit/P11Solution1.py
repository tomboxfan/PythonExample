current_month = int(input("What's the current month?"))

# rabbit_list[0] = 2, in the 1st month, there are 2 new born rabbits
rabbit_list = [2]

# rabbit_list[0]: 1st month
# rabbit_list[1]: 2nd month
for i in range(1, current_month):

    # Let's mimic the rabbit reproduction

    #i stands for month number.
    # Now, I am going to reproduce the rabbit for month i, see how many new born rabbits for month i.

    # Step 1) Let's put 0 for month i first. (Initially, there is 0 rabbit)
    rabbit_list.append(0)

    # Step 2) Let's reproduce
    # For example. Let's say how many rabbits can be born for month 5
    # Rabbits born in Month 1/2 can reproduce in month 5
    # Rabbits born in Month 1/2/3/4 can reproduce in month 7
    # Rabbits born in Month 1/2/3/4/i-3 can reproduce in month i
    # Loop from month 1 till month i -3
    for j in range(i-2):
        # if rabit_list[j] = 10, it means, there are 10 rabbits born in month j, and they can reproduce 10 rabbits
        # So I need to plus 10 to the current month i
        rabbit_list[i] += rabbit_list[j]


# All right! Rabbit reproduction done!
# Let's print how many rabbits are born for each month

month = 1
total_rabbit = 0
for k in rabbit_list:
    print(f"There are {k} rabbits born in month {month}")
    month+=1
    total_rabbit += k

print(f"There are {total_rabbit} rabbits in total.")