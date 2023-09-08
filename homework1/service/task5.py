def itersectionOfDiagonales(x1, x2, x3, x4):
    firstPossibleStraightLine = (x3[0] - x1[0]) / (x2[0] - x1[0]) == (x3[1] - x1[0]) / (x2[1] - x1[1])
    secondPossibleStraightLine = (x4[0] - x2[0]) / (x3[0] - x2[0]) == (x4[1] - x2[0]) / (x3[1] - x2[1])

    if firstPossibleStraightLine or secondPossibleStraightLine:
        return 0

    return [(x1[0] + x3[0]) / 2, (x1[1] + x3[1]) / 2]
