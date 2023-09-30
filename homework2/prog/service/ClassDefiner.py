import math as math


class ClassDefiner:

    def __init__(self, dotsAList, dotsBList):
        self.dotsAList = dotsAList
        self.dotsBList = dotsBList
        self.dotsANeighbourMap = {}
        self.dotsBNeighbourMap = {}
        self.dotsANeighbourCount = 0
        self.dotsBNeighbourCount = 0
        self.dotsANeighbourMapK = {}
        self.dotsBNeighbourMapK = {}

    def defineClass(self, k, c):
        self.calculateDotMaps(self.dotsAList, c)
        self.calculateDotMaps(self.dotsBList, c)

        dotsLens = list(self.dotsANeighbourMap.keys()) + list(self.dotsBNeighbourMap.keys())
        dotsLens.sort()
        self.calculateNeighbours(dotsLens, k)

        if self.dotsANeighbourCount > self.dotsBNeighbourCount:
            c.determinator = "I'm instance of A class"
        elif self.dotsANeighbourCount < self.dotsBNeighbourCount:
            c.determinator = "I'm instance of B class"
        elif self.calculateAverageDistance(self.dotsANeighbourMapK) > self.calculateAverageDistance(self.dotsBNeighbourMapK):
            c.determinator = "I'm instance of B class"
        else:
            c.determinator = "I'm instance of A class"

    def calculateDotMaps(self, dotsList, c):
        for element in dotsList:
            lenToC = math.sqrt(abs(element.x ** 2 - c.x ** 2 + element.y ** 2 - c.y ** 2))
            if dotsList == self.dotsAList:
                self.dotsANeighbourMap[lenToC] = element
            elif dotsList == self.dotsBList:
                self.dotsBNeighbourMap[lenToC] = element

    def calculateNeighbours(self, dotsLens, k):
        counter = 0
        for key in dotsLens:
            if counter == k:
                break

            if self.dotsANeighbourMap.__contains__(key):
                self.dotsANeighbourCount += 1
                self.dotsANeighbourMapK[self.dotsANeighbourMap.get(key)] = key

            if self.dotsBNeighbourMap.__contains__(key):
                self.dotsBNeighbourCount += 1
                self.dotsBNeighbourMapK[self.dotsBNeighbourMap.get(key)] = key

            counter += 1

    def calculateAverageDistance(self, dotsMap):
        dotsLenSum = 0
        counter = 1

        for elementLen in dotsMap.values():
            dotsLenSum += elementLen
            counter += 1

        return dotsLenSum / counter
