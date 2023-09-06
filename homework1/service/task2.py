def convertBinaryToDecimal(a):
    ans = 0
    counter = 1

    while a != 0:
        ans += (a % 10) * counter
        counter *= 2
        a = a // 10

    return ans
