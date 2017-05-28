def compare_char(seq):
    x = 0
    Alpha = {}
    while x < len(seq):
        if seq[x] in Alpha:
            Alpha[seq[x]] +=1
        if seq[x] not in Alpha:
                Alpha[seq[x]] =1
        x+=1
    return Alpha


print(compare_char('aabcccdefgghij'))



