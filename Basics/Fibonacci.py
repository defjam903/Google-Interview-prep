# Python program to display the Fibonacci sequence up to n-th term using recursive functions
import io

def Fibonacci(value):
    if value <=1:
        return value
    else:
        return (Fibonacci(value-1) + Fibonacci(value-2))


def TakeSomeSpace(value):
    with open("c:/temp/python/" + str(value)  + ".txt", "w") as f:
        f.write(Fibonacci(i) * '0')

value = 17567597987978967
for i in range(value):
    print(Fibonacci(i))
    TakeSomeSpace(i)

print('Complete')