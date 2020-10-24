base_number = int(input("Enter a one-digit number: "))
term_count = int(input("No. of terms: "))
x = 0
sum = 0

'''
The logic here is:
each term = previous term + (10^term_index) * base_number
'''
for i in range(0, term_count):
    x = x + int((10 ** i) * base_number)
    sum = sum + x
    print("+", x, end=' ')

print("=", sum)