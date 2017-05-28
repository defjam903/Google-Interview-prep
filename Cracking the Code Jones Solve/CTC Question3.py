def Urlfy(word, replace):
    L_word = len(word)
    x = 0
    newword = []
    while x <= L_word - 1:
        if word[x] == ' ':
            newword.append(replace)
        else:
            newword.append(word[x])
        x += 1
    return newword
print(''.join(Urlfy('Join the Stack Overflow Community' , '%20')))
