'''
这道题有几个看点
1) factorise 某个数主要是依次尝试prime number, 所以需要找到所有的prime number list
   这里使用了function - get_prime_number()

2)
'''

def get_prime_number():
    primes = []
    for i in range(2, 1000):
        sqr_root = int(i ** (1/2)) + 1
        for j in range(2, sqr_root):
            if i % j == 0:
                break
        else: # if break code is not triggered, else clause will be triggered
            primes.append(i)
    return primes



i = int(input("show me the number: "))

if i > 1000:
    print("Invalid number. You can only try number less than 1000")
    exit(0)

original = i

factor_list = []

prime_number_list = get_prime_number()
print("Now we have prime number list", prime_number_list)

# if it is prime number
if original in prime_number_list:
    print(original, '=', sep=' ', end=' ')
    print(1, original, sep=' * ', end=' ')
    exit(0)


factor_found = True

while factor_found:
    for f in prime_number_list:
        if i % f == 0:
            factor_list.append(f)
            i = i // f
            break
    else:
        factor_found = False





print(original, '=', sep=' ', end=' ')
print(*factor_list, sep=' * ', end=' ')

