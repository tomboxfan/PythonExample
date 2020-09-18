i = int(input("Number:"))
print(i)
original = i
factor_list = []

for j in range(2, i):
    while i % j == 0:
        factor_list.append(j)
        i = i / j

print(factor_list)

print(original, '= ', end='');
print(*factor_list, sep = ' * ');