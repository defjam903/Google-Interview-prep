def Does_it_count(word):
    D_words = {}
    i = 0
    while word != None:
        i+=1
        if word[i] in D_words:
            return True
        else:
            if word[i] not in D_words:
                D_words = {word[i]: +1}



print(Does_it_count('google'))