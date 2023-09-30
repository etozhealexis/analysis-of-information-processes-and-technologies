import random as random
from prog.model.A import A
from prog.model.B import B


class Generator:

    def generateAList(self, dotsCount):
        dotsList = []

        for i in range(0, dotsCount):
            dotsList.append(A(random.randint(0, 5), random.randint(5, 10)))

        return dotsList

    def generateBList(self, dotsCount):
        dotsList = []

        for i in range(0, dotsCount):
            dotsList.append(B(random.randint(5, 10), random.randint(0, 5)))

        return dotsList
