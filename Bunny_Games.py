simulation  = [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]


def Bunny_Float(matrix,x,y,strength):
    if matrix[x][y] == -1:
    	return
    elif matrix[x][y] <= strength:
        matrix[x][y] = -1
    elif matrix[x][y] > strength:
    	return
    if x > 0:
        Bunny_Float(matrix, x - 1, y,strength) #right
    if x < len(matrix[y]) - 1:
        Bunny_Float(matrix, x + 1, y,strength) #left
    if y > 0:
        Bunny_Float(matrix, x, y - 1,strength) #down
    if y < len(matrix) - 1:
        Bunny_Float(matrix, x, y + 1,strength)  #up
    return

Bunny_Float(simulation,2,1,5)
print(simulation)