# 题目017：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# built-in function. ord() / chr()
import string


def solution1():
    sentence = input('input a sentence:')
    count_summary = {
        'letter' : 0,
        'space' : 0,
        'digit' : 0,
        'others' : 0,
    }

    for c in sentence:
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
            count_summary['letter'] = count_summary['letter'] + 1
            # count_summary['letter'] += 1
        elif c == ' ':
            count_summary['space'] += 1
        elif '0' <= c <= '9':
            count_summary['digit'] += 1
        else:
            count_summary['others'] += 1

    print(count_summary)

# solution1()


def solution2():
    sentence = input('input a sentence:')
    count_summary = {
        'letter' : 0,
        'space' : 0,
        'digit' : 0,
        'others' : 0,
    }

    for c in sentence:
        if c in string.ascii_letters: # ascii_letters = ascii_lowercase + ascii_uppercase
            count_summary['letter'] = count_summary['letter'] + 1
            # count_summary['letter'] += 1
        elif c == ' ':
            count_summary['space'] += 1
        elif c in string.digits:
            count_summary['digit'] += 1
        else:
            count_summary['others'] += 1

    print(count_summary)

# solution2()

# 打印出每个字符出现的次数
def solution3():
    sentence = input('input a sentence:')
    count_summary = {}
    for c in sentence:
        if c in count_summary:
            count_summary[c] += 1 # update the entry for 'c'
        else:
            count_summary[c] = 1 # insert a new entry to the dictionary c:1

    print(count_summary)
solution3()