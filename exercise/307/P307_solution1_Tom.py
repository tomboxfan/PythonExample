# From Tom

def calculate_pi(n_terms):
    numerator = 4
    denominator = 1
    operation = 1
    pi = 0

    for i in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2
        operation *= -1

    return pi

print(calculate_pi(1000000))