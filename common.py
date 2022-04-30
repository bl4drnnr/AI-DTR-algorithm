
def informationGain(X):
    totalSumOfX = 0

    if type(X[0]) is int:
        totalSumOfX = sum(X)
    else:
        for x in X:
            totalSumOfX += x[0]
            totalSumOfX += x[1]

    return
