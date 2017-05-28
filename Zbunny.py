simulation  = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]

def Z_Bunny(SIM, x, y, strength):
    for i in range(len(SIM)):
        for j in range(len(SIM[i])):
            if j != len(SIM[i])- 1:
                if SIM[i][j] <= strength:
                    SIM[i][j] = -1
    return SIM



for i in range(0,len(Z_Bunny(simulation,0,0,2))):
        print simulation[i]
