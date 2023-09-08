def sumOfNumbers(a):
    ans = 0

    while a > 0:
        ans += a % 10
        a //= 10

    return ans
