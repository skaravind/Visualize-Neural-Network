class Node:
    def __init__(self, layers, lno, nodes, i, r):
        self.layers = layers
        partx = self.layers - 1
        party = nodes + 1
        self.x = (lno-1)*width/(partx)
        if lno == 1:
            self.x = self.x + 50
        if lno == layers:
            self.x = self.x - 50
        self.y = (i+1)*height/party
        self.r = r
    
    def show(self):
        ellipse(self.x, self.y, self.r, self.r)