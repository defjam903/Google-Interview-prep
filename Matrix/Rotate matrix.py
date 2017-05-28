matrix =[[1,2,3,4],
        [6,7,8,9],
        [11,12,13,14],
        [16,17,18,19]]


def Find_Neo(Blue_Pill):
    for n in range(0,len(Blue_Pill) -1):
        for m in range(n+1, len(Blue_Pill)):
            Blue_Pill[n][m] , Blue_Pill[m][n] = Blue_Pill[m][n] , Blue_Pill[n][m]
    return Blue_Pill

for row in Find_Neo(matrix):
    print(row[::1])