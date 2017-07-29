class QuadTree:

    def __init__(self, xmin, xmax, ymin, ymax):
        self.rootNode = QuadTreeNode(xmin, xmax, ymin, ymax)

    def findVals(x, y):
        return self.rootNode.findVals(x,y)

    def addVal(val):
        self.rootNode.addVal(val)
