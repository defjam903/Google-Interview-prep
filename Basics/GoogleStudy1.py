def GetSum(glist,sum):
    x = 0
    arrayl = len(glist) - 1
    while x < arrayl:
        x += 1
        arrayl -= 1

        if glist[x] + glist[len(glist) - x] == sum:
            print(x ,arrayl)
            return True
        elif glist[x] == sum or glist[len(glist) - x] == sum:
            print(x , arrayl)
            return True






#googlelist = [1, 2, 5, 66, 2, 88, 3, 2, 4, 11, 3, 44, 32, 2, 7, 21, 66, 2, 88, 2, 2, 3];


googlelist = [1, 2, 3, 4, 4, 5, 6, 7, 9];


print(GetSum(googlelist, 8))

