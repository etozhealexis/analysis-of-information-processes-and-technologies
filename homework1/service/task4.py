def sumOfNumbers(a):
    counter = 0

    while a > 10:
        for i in str(a):
            counter += int(i)

        a = counter
        counter = 0

    return a
