table = {'1985': 'Test movie' , '1983': 'Test Movie2' , '2000': 'Test Movie 3'}

year = '1983'
movie = table[year]
print(movie)

for year in table:
    print(year + '\t' + movie + '\t')