import matplotlib.pyplot as plt
from prog.model.A import A
from prog.model.B import B
from typing import List


class Renderer:

    def __init__(self, dotsAList: List[A], dotsBList: List[B], c, k):
        self.dotsAList = dotsAList
        self.dotsBList = dotsBList
        self.c = c
        self.k = k

    def drawDots(self):

        aXList = self.getXList(self.dotsAList)
        aYList = self.getYList(self.dotsAList)
        bXList = self.getXList(self.dotsBList)
        bYList = self.getYList(self.dotsBList)

        plt.scatter(aXList, aYList, c='red')
        plt.scatter(bXList, bYList, c='blue')
        plt.scatter(self.c.x, self.c.y, c='yellow')
        plt.plot()
        plt.show()

    def getXList(self, dotsList):
        dotsX = []
        for element in dotsList:
            dotsX.append(element.x)
        return dotsX

    def getYList(self, dotsList):
        dotsY = []
        for element in dotsList:
            dotsY.append(element.y)
        return dotsY
