target_month = int(input("What's the current month?"))

# key: month. 1/2/3/4/5
# value: rabbit list. ["Rabbit", "Rabbit"...]
rabbit_dict = {}

# Step 1) Insert empty list for each month
for i in range(1, target_month + 1):
    rabbit_dict[i] = []

# Step 2) Initally, there are 2 rabbits in the 1st month
rabbit_dict[1] += ["Rabbit", "Rabbit"]

# Step 3) Let's mimic the rabbit reproduction
for i in range(1, target_month+1):

    # here, i stands for month number.
    # rabbits from month 1, can reproduce in month 4/5/6/...23
    # rabbits from month 5, can reproduce in month 8/9/10/...23

    # rabbits in month i can reproduce in all months from i+3 till target_month
    for j in range(i+3, target_month + 1):
        # Question? month i, how many rabbits?
        # Answer: rabbit_dict[i] 这么多只
        rabbit_dict[j] += rabbit_dict[i]



# All right! Rabbit reproduction done!
# Let's print how many rabbits are born for each month

total_rabbit = 0
for month,rabbits in rabbit_dict.items():
    print(f"Month {month}: {rabbits}")
    total_rabbit += len(rabbits)

print(f"There are {total_rabbit} rabbits in total.")