# Python Program to display the powers of 2 using anonymous function

# sets how many terms there is as a integer
terms = 10000
to_the_power = 208

#using an anonymous function
result = list(map(lambda x: to_the_power ** x , range(terms)))

for i in range(terms):
    print(' Line number:' , i, ' 2 raised to the power of ',to_the_power , 'is' , result[i])

