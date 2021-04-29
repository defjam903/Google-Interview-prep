matrix =[[1,2,3,4],
        [6,0,8,9],
        [11,12,13,14],
        [16,17,0,19]]


def Convert_to_0(Neo):
    FirstRow = False
    FirstCol = False

# test first column 0 or not
    for col in range(0,len(Neo) - 1):
        if Neo[col][0] == 0:
            FirstCol == True

# test first row 0 or not
    for row in range(0, len(Neo)):
            if Neo[0][row] == 0:
                FirstRow == True

# mark 0 on first row and column
    for n in range(0, len(Neo) - 1):
        for m in range(n + 1, len(Neo)):
            if Neo[n][m] == 0:
                Neo[n][0] = 0
                Neo[0][m] = 0

# use mark to set elements
    for n in range(0, len(Neo) - 1):
        for m in range(n + 1, len(Neo)):
            if  Neo[n][0] or  Neo[o][m] == 0:
                Neo[n][m] == 0

# set first column and row
    i = 0
    if FirstCol:
        while i < len(Neo):
            Neo[i][0] == 0

    i = 0
    if FirstRow:
        while i < len(Neo):
            Neo[0][i] == 0



    return Neo



for row in Convert_to_0(matrix):
    print(row[::1])
