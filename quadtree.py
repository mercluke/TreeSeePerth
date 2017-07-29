class QuadTreeNode:
    #const
    MAX_VALUES = 1500

    def size(self):
        if self.root:
            return len(self.values)
        else:
            count = 0
            for i in range(0,4):
                count += self.children[i].size()
            return count

    def addVal(self,val):
        if self.root:
            self.values.append(val)
            if len(self.values) >= self.MAX_VALUES:
                self.root = False
                #print('splitting root node')
                self.splitRootNode()
            else:
                pass
                #print('apparently ' + str(len(self.values)) + ' < ' + str(self.MAX_VALUES))
        else:
            if float(val['lon']) < self.x_mid:
                if float(val['lat']) < self.y_mid:
                    self.children[0].addVal(val)
                else:
                    self.children[2].addVal(val)
            else:
                if float(val['lat']) < self.y_mid:
                    self.children[1].addVal(val)
                else:
                    self.children[3].addVal(val)

    def isRoot(self):
        return self.root

    def splitRootNode(self):
        self.children[0] = QuadTreeNode(self.x_min_bound, self.x_mid, self.y_min_bound, self.y_mid)
        self.children[1] = QuadTreeNode(self.x_mid, self.x_max_bound, self.y_min_bound, self.y_mid)
        self.children[2] = QuadTreeNode(self.x_min_bound, self.x_mid, self.y_mid, self.y_max_bound)
        self.children[3] = QuadTreeNode(self.x_mid, self.x_max_bound, self.y_mid, self.y_max_bound)
        for val in self.values:
            self.addVal(val)
        del self.values[:]

    def findVals(self,x, y):
        if self.root:
            return self.values[:]
        else:
            if x < self.x_mid:
                if y < self.y_mid:
                    return self.children[0].findVals(x,y)
                else:
                    return self.children[2].findVals(x,y)
            else:
                if y < self.y_mid:
                    return self.children[1].findVals(x,y)
                else:
                    return self.children[3].findVals(x,y)

    def  __init__(self, xmin, xmax, ymin, ymax):
        self.root = True
        self.x_min_bound = xmin
        self.x_max_bound = xmax
        self.y_min_bound = ymin
        self.y_max_bound = ymax

        #calculate midpoint for child node's bounds
        self.x_mid = (self.x_min_bound+self.x_max_bound) / 2.0
        self.y_mid = (self.y_min_bound+self.y_max_bound) / 2.0

        #unused if root node, only gets crafted if
        #len(values) ever exceeds MAX_VALUES
        self.children = [None, None, None, None]
        self.values = []

class QuadTree:

    def __init__(self, xmin, xmax, ymin, ymax):
        self.rootNode = QuadTreeNode(xmin, xmax, ymin, ymax)

    def findVals(self,x, y):
        return self.rootNode.findVals(x,y)

    def addVal(self,val):
        self.rootNode.addVal(val)
