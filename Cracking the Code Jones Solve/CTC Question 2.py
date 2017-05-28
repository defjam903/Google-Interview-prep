
import sys
sys.setrecursionlimit(1500)

def Big_Perm(Word):
    if len(Word) == 0:
        return []
    if len(Word) == 1:
        return Word

    L = []
    for i in range(len(Word)):
        m = Word[i]
        result = Word[:1] + Word[i+1:]
        for p in Big_Perm(result):
            L.append([m] + p)
        return L


print(Big_Perm('google'))