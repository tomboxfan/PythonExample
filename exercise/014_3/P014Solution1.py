

def factorise(target_num):
    original = target_num

    # I need a list to store all factors of target_num
    factor_list = []


    # solution 1
    # for prime_factor in range(2, target_num+1):
    #
    #     # because there could be multiple same prime_factors in target_num
    #     # So we should use while
    #     # e.g. 125 = 5 ** 3
    #     while target_num % prime_factor == 0:
    #         factor_list.append(prime_factor)
    #
    #         # I remove prime_factor from target_num
    #         target_num = target_num / prime_factor


    #solution 2
    prime_factor = 2
    # because there could be multiple same prime_factors in target_num
    while (prime_factor <= original):
        if target_num % prime_factor == 0:
            target_num = target_num / prime_factor
            factor_list.append(prime_factor)
        else:
            prime_factor += 1


    # Let's print the expression ---------------------
    print(original, '= ', end='')
    if len(factor_list) == 1:
        print(1, "* ", end= '')

    # list expansion
    print(*factor_list, sep = ' * ')
    # -------------------------------------------------





for i in range(2, 1000):
    factorise(i)
