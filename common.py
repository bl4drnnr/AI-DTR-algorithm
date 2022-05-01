import math
from parser import getData
INPUT_DATA_LENGTH = len(getData())
GENERATED_TREE = []


def informationGainForClass(gainsPerAttribute, gainsPerAttributeItems):
    infoGainForClass = 0

    for x, gain in enumerate(gainsPerAttribute):
        infoGainForClass += (sum(gainsPerAttributeItems[x])/INPUT_DATA_LENGTH) * gain

    return float(format(infoGainForClass, ".3f"))


def information(X):
    infoGain = 0

    totalSumOfX = sum(X)
    for x in X:
        infoGain += informationEntropy(x, totalSumOfX)

    return float(format(infoGain, ".3f"))


def informationEntropy(x, y):
    if x == 0 or y == 0:
        return 0
    return -1 * (x/y) * math.log2((x/y))


def countItems(array):
    result = {}
    for item in array:
        if result.get(item) is None:
            result[item] = 1
        else:
            result[item] += 1

    return result


def extractTreeData(data):
    gainsList = []
    for attr, value in data.items():
        gainsList.append(value['gain'])

    for attr, value in data.items():
        if value['gain'] == max(gainsList):
            return generateTree(attr, data)


def generateTree(node, nextData):
    GENERATED_TREE.append(node)

    # Check if node has generated rule

    # Sort data in node, just to make it print in right way
    sortedNodeData = {}
    for item in sorted(nextData[node].values()):
        for attr, value in nextData[node].items():
            if item == value:
                sortedNodeData[attr] = value

    for attr, value in sortedNodeData.items():
        if value == 0 and attr != 'gain' and attr != 'qor':
            GENERATED_TREE.append(f"\t-- {attr} -- {sortedNodeData['qor']}")
        elif attr != 'gain' and attr != 'qor':
            GENERATED_TREE.append(f"\t-- {attr} --")

    for attr, value in nextData.items():
        if attr != node:
            print(attr, value)


def printTree():
    for item in GENERATED_TREE:
        print(item)
