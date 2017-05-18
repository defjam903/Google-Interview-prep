friend = {
    'chris': '6451',
    'holly': '8941'
}

friend['sherry'] = '5335'
print(friend['sherry'], end='\n')

for key in friend:
    print(key, ":", friend[key], end='\n')