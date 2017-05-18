# Python program to find the L.C.M. of two input number

def GCD(x,y):
    while(y):
      x,y = y, x % y
    return x

def findLCM(x,y):
    lcm = (x*y)//GCD(x,y)
    return lcm


num1 = 2246645654645
num2 = 86545465465469

print('the LCM of the two numbers are ' , findLCM(num1,num2))
