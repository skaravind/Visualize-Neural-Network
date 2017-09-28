import Nodes, Synapse
from Training import *
layers = 3
r = 60
iter = 1
flag = False
FR = 2
syn0 = [[random(-1,1) for _ in range(4)] for _ in range(3)]
syn1 = [[random(-1,1) for _ in range(1)] for _ in range(4)]

def createNodes(ns, layerNo):
    for i in range(ns):
        node = Nodes.Node(layers,layerNo,ns,i, r)
        node.show()
        nodes.append(node)

def createSynapse(IN,HN,ON):
    for i in range(IN):
        for j in range(IN,IN+HN):
            synapse = Synapse.Synapse(nodes[i].x,nodes[i].y,nodes[j].x,nodes[j].y)
            synapse.show()
            synapses.append(synapse)
    for i in range(IN,IN+HN):
        for j in range(IN+HN,IN+HN+ON):
            synapse = Synapse.Synapse(nodes[i].x,nodes[i].y,nodes[j].x,nodes[j].y)
            #synapse.show()
            synapses.append(synapse)

def setup():
    global net,layers,nodes,synapses,r,syn0,syn1
    nodes = []
    synapses = []
    size(600,600)
    background(255)
    stroke(0)
    strokeWeight(0)

    Inodes = 3
    Hnodes = 4
    Onodes = 1
    
    #input layer
    fill (0,200,0)
    createNodes(Inodes, 1)

    #hidden layer
    fill (200,200,0)
    createNodes(Hnodes, 2)

    #output layer
    fill (0,0,255)
    createNodes(Onodes, 3)
    
    #synapses
    createSynapse(Inodes,Hnodes,Onodes)
    
    fill (26,100,255)
    textAlign(CENTER)
    textFont(createFont('Georgia',16))
    frameRate(FR)

def draw():
    global syn0, syn1, iter, flag, FR
    setup()
    stroke(255,0,0)
    syn0,syn1,error = TuneWeights(syn0,syn1)
    syn = 0
    for i in range(len(syn0)):
        for j in range(len(syn0[0])):
            stwt = map(abs(syn0[i][j]),0,15,0,15)
            strokeWeight(stwt)
            synapses[syn].show()
            syn += 1
    for i in range(len(syn1)):
        for j in range(len(syn1[0])):
            stwt = map(abs(syn1[i][j]),0,15,0,15)
            strokeWeight(stwt)
            synapses[syn].show()
            syn += 1
    text('|ERROR| = %f' % abs(error[0][0]), width/2, height - 50)
    text('ITERATIONS = %d' % iter, width/2, height - 30)
    text('R = RESTART or S = SPEED UP or P = STOP', width/2, height - 10)
    iter += 1
    if flag:
        noLoop()

def keyPressed():
    global iter,syn0,syn1, flag, FR
    if key == ('r'or'R'):
        iter = 1
        syn0 = [[random(-1,1) for _ in range(4)] for _ in range(3)]
        syn1 = [[random(-1,1) for _ in range(1)] for _ in range(4)]
        FR = 2
        setup()
    elif key ==('p' or 'P'):
        flag = True
    elif key==('s' or 'S'):
        FR+=2