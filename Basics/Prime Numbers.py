# Python program to check if the input number is prime or not


def Isprime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return False
            else:
                return True
    else:
        return False


print('the given number returned ', Isprime(36574589675489), 'for prime')

