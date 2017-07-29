class QuadTreeNode:
    #const
    MAX_VALUES = 20

    def size():
        return len(self.values)

    def addVal(val):
        self.values.append(val)
        if len(self.values) >= MAX_VALUES:
            self.splitRootNode()

    def isRoot():
        return self.children[0] is None

    def splitRootNode():
        if not self.isRoot():
            self.children[0] = QuadTreeNode(self.x_min_bound, self.x_mid, self.y_min_bound, self.y_mid)
            self.children[1] = QuadTreeNode(self.x_mid, self.x_max_bound, self.y_min_bound, self.y_mid)
            self.children[2] = QuadTreeNode(self.x_min_bound, self.x_mid, self.y_mid, self.y_max_bound)
            self.children[3] = QuadTreeNode(self.x_mid, self.x_max_bound, self.y_mid, self.y_max_bound)
            for val in self.values:
                if float(val['lon']) < x_mid:
                    if float(val['lat']) < y_mid:
                        self.children[0].addVal(val)
                    else:
                        self.children[2].addVal(val)
                else:
                    if float(val['lat']) < y_mid:
                        self.children[1].addVal(val)
                    else:
                        self.children[3].addVal(val)
            del self.values[:]

    def  __init__(self, xmin, xmax, ymin, ymax):
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
