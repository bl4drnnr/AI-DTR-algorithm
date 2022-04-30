import math


def informationGain(X):
    totalSumOfX = 0
    infoGain = 0

    if type(X[0]) is int:
        totalSumOfX = sum(X)
        for x in X:
            infoGain += informationEntropy(x, totalSumOfX)
    else:
        for x in X:
            totalSumOfX += x[0]
            totalSumOfX += x[1]
        for x in X:
            infoGain += informationEntropy(x[0] + x[1], totalSumOfX)

    return infoGain


def informationEntropy(x, y):
    return -1 * (x/y) * math.log2((x/y))


def countItems(array):
    result = {}
    for item in array:
        if result.get(item) is None:
            result[item] = 1
        else:
            result[item] += 1
    print("result:", result)
    return result
