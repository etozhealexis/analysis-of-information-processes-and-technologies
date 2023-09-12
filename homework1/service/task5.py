def itersectionOfDiagonales(x1, x2, x3, x4):
    firstLine = (x4[0] - x1[0]) * (x2[0] - x1[0]) - (x4[1] - x1[1]) * (x2[1] - x1[1])
    secondLine = (x4[0] - x2[0]) * (x3[0] - x2[0]) - (x4[1] - x2[1]) * (x3[1] - x2[1])
    thirdLine = (x4[0] - x3[0]) * (x1[0] - x3[0]) - (x4[1] - x3[1]) * (x1[1] - x3[1])
    fourthLine = (x1[0] - x3[0]) * (x2[0] - x3[0]) - (x1[1] - x3[1]) * (x2[1] - x3[1])

    if firstLine * secondLine * thirdLine * fourthLine > 0:
        return 'Не прямоугольник'

    return [(x1[0] + x3[0]) / 2, (x1[1] + x3[1]) / 2]
