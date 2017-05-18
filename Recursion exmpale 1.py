# An example of a recursive function to
# find the factorial of a number
import sys

sys.setswitchinterval(sys.maxsize)

def calc_factorials_recursion(value):
    if value == 1:
        return 1
    else:
        return (value * calc_factorials_recursion(value - 1))



value = 22
print('The factorials of ' , value , 'is ', calc_factorials_recursion(value))