month = int(input("What's the current month?"))

rabbit_1m_old = 2
rabbit_2m_old = 0
rabbit_3m_old = 0
rabbit_adult = 0

# 历史重现！

# Loop reproduction

for i in range(month-1):

    # 3m old -> adult
    rabbit_adult += rabbit_3m_old;

    # 2m old -> 3m old
    rabbit_3m_old = rabbit_2m_old

    # 1m old -> 2m old
    rabbit_2m_old = rabbit_1m_old

    # adult reproduce 1m old
    rabbit_1m_old = rabbit_adult

    print('month %d rabbit total: ' % (i + 2), rabbit_1m_old + rabbit_2m_old + rabbit_3m_old + rabbit_adult, '-----------------------------------')
    print('1 month old rabbit: ', rabbit_1m_old)
    print('2 month old rabbit: ', rabbit_2m_old)
    print('3 month old rabbit: ', rabbit_3m_old)
    print('adult rabbit: ', rabbit_adult)