class Node:
    def __init__(self, point, map):
        self.location = point
        self.data = map[point][1]
        self.neighbors = []
        self.visited = False
        self.path = []

    def setNewNode(self, point, map):
        #self.location = self.getLocation(point)
        #self.data = self.getData(map, point)
        self.neighbors = self.findValidNeighbors(point, map)

    def getLocation(self, point):
        self.location = point

    def getData(self, map, point):
        self.data = map[point][1]


    def isVisited(self, prevVisited):
        for number in prevVisited:
            if self.location == number:
                return True
            else:
                return False


    def setPath(self, previousNode):
        if previousNode.path == []:
            self.path.append(self.location)
        else:
            self.path.append(previousNode.path)

        return self.path


#Rething this method. not logical to pass in the data for each neighboring node. Need to check the data at the map point
#not actually pass in a data value to the function. just pass the map
    def findValidNeighbors(self, point, map):
        if ((point % 10 != 0) and (map[point - 1][1] != 'W')):
            leftNeighbor = point - 1
            self.neighbors.append(leftNeighbor)

        if (not((point - 10) < 0)) and (map[point - 10][1] != 'W'):
            topNeighbor = point - 10
            self.neighbors.append(topNeighbor)

        remainder = (point + 1) % 10
        if (remainder != 0) and (map[point +1][1] != 'W'):
            rightNeighbor = point + 1
            self.neighbors.append(rightNeighbor)

        if (not (point + 10) > 99) and (map[point +10][1] != 'W'):
            bottomNeighbor = point + 10
            self.neighbors = self.neighbors.append(bottomNeighbor)

        return self.neighbors