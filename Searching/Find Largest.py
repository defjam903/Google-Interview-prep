
def FindLargestNumber(num1, num2,num3):
    if num1 >= num2 and num1 >= num3:
        return  num1
    elif num2 >= num1 and num2 >= num3:
        return  num2
    else:
        return  num3

num1 = 22
num2 = 54
num3 = 22

print("The largest number in the set is " ,  FindLargestNumber(num1,num2,num3))




