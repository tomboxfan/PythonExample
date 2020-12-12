'''
019 Requirement:
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。


High Level Design:
1) Find all numbers smaller than 1000, so it should be:

    for candidate in range(2,1001):
        pass

2) For each candidate, we need to check whether it is a perfect number or not. To do that, we need to:

   2.1) Find all factors of the candidate. (1 included, itself not included)

        factor_list = []
        for potential_factor in range(1, candidate):
            if candidate % potential_factor == 0:
               factor_list.append(potential_factor)

   2.2) Check whether their sum equals to candidate or not

        we can use built-in function sum() to do it
'''

for candidate in range(2, 1001):
    factor_list = []
    for potential_factor in range(1, candidate):
        if candidate % potential_factor == 0:
            factor_list.append(potential_factor)

    if sum(factor_list) == candidate:
        print(candidate)