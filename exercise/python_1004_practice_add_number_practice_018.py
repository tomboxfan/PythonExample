# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

def solution1_math(base_number:int, term_count:int) -> int:
    '''
    Use math to calculate the number in each term
    '''

    # time complexity - O(n^2)
    sum = 0
    for term_no in range(term_count):

        # Step 1) Calculate value_for_this_term

        # term 0 - 5
        #               Loop 0 times [ * 10 + 5]

        # term 1 - 55 = 5 * 10 + 5
        #               Loop 1 times [ * 10 + 5]

        # term 2 - 555 = (5 * 10 + 5) * 10 + 5
        #               Loop 2 times [ * 10 + 5]

        # term 3 - 5555 = ((5 * 10 + 5) * 10 + 5) * 10 + 5
        #               Loop 3 times [ * 10 + 5]

        value_for_this_term = base_number

        # "_" is throwaway variable - we don't need this variable, we want to ignore it
        for _ in range(term_no):
            value_for_this_term = value_for_this_term * 10 + base_number

        sum = sum + value_for_this_term

    return sum


def solution2_math_optimize(base_number:int, term_count:int) -> int:
    '''
    Use math to calculate the number in each term
    '''

    # time complexity - O(n)
    sum = 0
    value_for_this_term = base_number
    sum += value_for_this_term

    for term_no in range(term_count - 1):

        # Step 1) Calculate value_for_this_term

        # term 0 - 5
        # term 1 - 55 = (term0 * 10) + 5
        # term 2 - 555 = (term1 * 10) + 5
        # term 3 - 5555 = (term2 * 10) + 5
        value_for_this_term = value_for_this_term * 10 + base_number
        sum = sum + value_for_this_term

    return sum


def solution3_math2(base_number, term_count):
    '''
    Calculate the sum directly from those numbers
    '''
    sum = 0
    for term_no in range(term_count):
        for j in range(term_no+1):
            sum += 10 ** j

    return sum * base_number


def solution4_math2_optimized(base_number, term_count):
    '''
    Calculate the sum directly from those numbers
    '''
    sum = 0
    for term_index in range(1, term_count + 1):
        sum += 10 ** (term_index - 1) * (term_count + 1 - term_index) * base_number
    return sum

def solution5_math3_yixuan(base_number, term_count):
    value_for_this_term = 0
    sum = 0
    for i in range(0, term_count):
        value_for_this_term = value_for_this_term + int(10 ** i * base_number)
        sum += value_for_this_term
    return sum



def solution6_str_manipulation(base_number, term_count):
    '''
    Use string manipulation to ge the number in each term
    '''
    sum = 0
    for term_index in range(1, term_count + 1):
        sum += int(str(base_number) * term_index)
    return sum

def solution7_eval(base_number, term_count):
    '''
    Use built-in function eval() to calculate the result
    '''

    #s=2+22+222+2222+22222
    expression = ''
    for term_index in range(1, term_count+1):
        expression += str(base_number) * term_index
        if term_index < term_count:
            expression += '+'

    print("Expression:", expression)
    sum = eval(expression)
    return sum





base_number = int(input("Enter the base number: "))
term_count = int(input("Enter the entry count: "))

result = solution1_math(base_number, term_count)
print("The answer is", result)

result = solution2_math_optimize(base_number, term_count)
print("The answer is", result)

result = solution3_math2(base_number, term_count)
print("The answer is", result)

result = solution4_math2_optimized(base_number, term_count)
print("The answer is", result)

result = solution5_math3_yixuan(base_number, term_count)
print("The answer is", result)

result = solution6_str_manipulation(base_number, term_count)
print("The answer is", result)

result = solution7_eval(base_number, term_count)
print("The answer is", result)

