from itertools import islice

def n_grams(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(n_grams(a, 4))