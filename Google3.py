friend = {
    'chris': '111',
    'holly': '2223'
}

friend['sherry'] = '23234'
print(friend['sherry'], end='\n')

for key in friend:
    print(key, ":", friend[key], end='\n')
