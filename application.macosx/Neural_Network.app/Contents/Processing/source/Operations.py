def sigm(x):
    e = 2.718
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] = 1/(1+e**(-x[i][j]))
    return x

def dotProd(x,y):
    xx = len(x)
    xy = len(x[0])
    yx = len(y)
    yy = len(y[0])
    result = [[None for _ in range(yy)] for _ in range(xx)]
    for ix in range(xx):
        for jy in range(yy):
            sum = 0
            for jx in range(xy):
                sum += x[ix][jx]*y[jx][jy]
            result[ix][jy] = sum 
    return result

def subtract(x,y):
    if x==1:
        x = [[1 for _ in range(len(y[0]))] for _ in range(len(y))]
    result = [[None for _ in range(len(x[0]))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] - y[i][j]
    return result

def prod(x,y):
    if x==10:
        x = [[10 for _ in range(len(y[0]))] for _ in range(len(y))]
    result = [[None for _ in range(len(x[0]))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] * y[i][j]
    return result

def add(x,y):
    result = [[None for _ in range(len(x[0]))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
    return result

def T(x):
    result = [[None for _ in range(len(x))] for _ in range(len(x[0]))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[j][i] = x[i][j]
    return result