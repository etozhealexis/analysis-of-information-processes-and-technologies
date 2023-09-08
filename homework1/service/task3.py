def simplicityOfNumber(a):
    endOfRange = int(a ** 1 / 2)

    for i in range(2, endOfRange):
        if a % i == 0:
            return False

    return True
