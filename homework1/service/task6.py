def maxVolume(heights):
    ans = 0
    maxHeight = max(heights)
    firstPossibleMax = 0
    secondPossibleMax = 0

    i = 1
    while i < len(heights):
        currentHeight = i - 1
        while heights[currentHeight] > heights[i]:
            i += 1

        ans += (i - currentHeight) * heights[currentHeight]

        if heights[i] == maxHeight:
            firstPossibleMax = i
            break
        i += 1

    i = len(heights) - 2
    while i > 1:
        currentHeight = i + 1
        while heights[currentHeight] > heights[i]:
            i -= 1

        ans += (currentHeight - i) * heights[currentHeight]

        if heights[i] == maxHeight:
            secondPossibleMax = i
            break
        i -= 1

    if firstPossibleMax != secondPossibleMax:
        ans += abs(secondPossibleMax - firstPossibleMax) * maxHeight

    return ans
