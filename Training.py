from Operations import *
'''
lines = loadStrings("/Users/Karan/Desktop/Processing/Neural_Network/data.csv")
X = [[],[],[],[]]
y = [[]]
for i in range(4):
    for j in range(3):
        X[i].append(int(lines[i+1].split(',')[j]))
    y[0].append(int(lines[i+1].split(',')[3]))

y = T(y)
'''
X = [[0,0,1],[1,1,1],[1,0,1],[0,1,1]]
y = [[0],[1],[1],[0]]

lr = 10

def TuneWeights(syn0,syn1):
    text('TRAINING....', width/2, 30)
    for i in range(len(y)):
        text('[%d, %d, %d]'%(X[i][0],X[i][1],X[i][2]),50,(i+1)*height/25)
        text('[%d]'%y[len(y)-i-1][0],width-50,height/2 - (i+2)*height/20)
    l1 = dotProd(X,syn0)
    l1 = sigm(l1)
    l2 = dotProd(l1,syn1)
    l2 = sigm(l2)
    l2_del = prod(subtract(y,l2),prod(l2,subtract(1,l2)))
    l1_del = prod(dotProd(l2_del, T(syn1)), prod(l1,subtract(1,l1)))
    syn1 = add(syn1, prod(lr,dotProd(T(l1), l2_del)))
    syn0 = add(syn0, prod(lr,dotProd(T(X), l1_del)))
    for i in range(len(l2)):
        text('[%.2f]'%l2[i][0],width-50,height/2 + (i+2)*height/20)
    return syn0, syn1, subtract(y,l2)