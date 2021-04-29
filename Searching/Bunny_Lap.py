def getoverlap(a,b):
    return max(0,min(a[1],b[1]) - max(a[0],b[0]))



print(getoverlap( [[1, 3], [3, 6]]))