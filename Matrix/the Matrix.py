import copy

def rotate(matrix):
    data = copy.depcopy(matrix)
    for i in range(len(data)):
        for j  in range(i+1, len(data[i])):
            temp = data[i][j]
            data[i][j] = data[j][i]
            data[j][i] = temp

    return data

D =[[1, 2, 3, 4],
   [4, 5, 6, 89],
   [7, 8, 9, 33]]

print(rotate)