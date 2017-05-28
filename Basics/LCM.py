# The least common multiple (L.C.M.) of two numbers
# is the smallest positive integer that is perfectly
# divisible by the two given numbers.

def LCM_Funct(x,y):
    if x > y:
        greater = x
    else:
        greater = y
        while(True):
            if (greater % x == 0 ) and ( greater % y == 0 ):
                lcm = greater
                break
            greater +=1
    return lcm

num1 = 33675858
num2 = 79887686
print('The LCM of', num1, 'and', num2, 'is' , LCM_Funct(num1,num2))

