import math


def informationGain(X):
    totalSumOfX = 0

    if type(X[0]) is int:
        totalSumOfX = sum(X)
        return informationEntropy(X[0]/totalSumOfX, X[1]/totalSumOfX)
    else:
        for x in X:
            totalSumOfX += x[0]
            totalSumOfX += x[1]


def informationEntropy(x, y):
    return -1 * x * math.log2(x) - y * math.log2(y)
