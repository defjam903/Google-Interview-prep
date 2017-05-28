def Compare_one(word1,word2):
    WD1 = len(word1)
    WD2 = len(word2)
    x = 0
    y = 0
    if WD1> WD2+1 or WD2 > WD1 +1:
        return False

    while x < WD1:
        if word1[x] == word2[x]:
            y+=1
        if y == WD1-1 or WD1 +1:
            return True
        if y == WD2 -1 or WD2 +1:
            return True
    x+=1
print(Compare_one('car','cart'))

