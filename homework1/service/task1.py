def NOD(a, b):
    while True:
        if (a > b) and (a % b == 0):
            ans = b
            break
        elif (b > a) and (b % a == 0):
            ans = a
            break

        if a > b:
            a %= b
        else:
            b %= a

    return ans
