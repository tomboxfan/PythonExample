# def square(x):
#     return x ** 2
#
# print(square(10))
# print(square(20))
# print(square(30))
# print(square(40))
#
# def launch_missile():
#     print("Missle launched!")
#
# launch_missile()
# launch_missile()
# launch_missile()
#
# def nth_root(radicand, n):
#     return radicand ** (1/n)
#
# print(nth_root(4,2))
# print(nth_root(27,3))
# print(nth_root(625,4))

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("I love Python")
# banner("I love Python", "*")
# banner("Singapore is a beautiful city")
# banner("Singapore is a beautiful city", "-")