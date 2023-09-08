def convertBinaryToDecimal(a):
    ans = 0
    counter = 1

    while a != 0:
        ans += (a % 10) * counter
        counter *= 2
        a //= 10

    return ans


def convertDecimalToBinary(a):
    ans = ""

    while a != 0:
        ans += str(a % 2)
        a //= 2

    return int(ans[::-1])
