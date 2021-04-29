# Python Program to find the factors of a number


def print_factors(number):
    print('The factors of ' ,number, 'is')
    for i in range(1,number + 1):
        if number % i == 0:
           print(i)

num1 = 320

print(print_factors(num1))
