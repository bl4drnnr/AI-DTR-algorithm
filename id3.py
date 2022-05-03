from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute
from common import information, extractTreeData, printTree, getAllPossibleSubsets, getInformationEntropyPerSubset

DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
INPUT_DATA_LENGTH = len(DATA)

# Find information entropy for decision attribute
recordsPerDecisionAttribute = {}
quantityOfRecordsPerDecisionAttribute = []
for record in DATA:
    if recordsPerDecisionAttribute.get(record[KEY_ATTRIBUTE]) is None:
        recordsPerDecisionAttribute[record[KEY_ATTRIBUTE]] = 1
    else:
        recordsPerDecisionAttribute[record[KEY_ATTRIBUTE]] += 1

for attr, value in recordsPerDecisionAttribute.items():
    quantityOfRecordsPerDecisionAttribute.append(value)

DECISION_CLASSES_INFO_GAIN = information(quantityOfRecordsPerDecisionAttribute)

# Divide input data on subsets by attributes
ALL_POSSIBLE_SUBSETS_ITEMS = {}

for attr, value in ALL_POSSIBLE_ATTRIBUTES.items():
    if attr != KEY_ATTRIBUTE:
        ALL_POSSIBLE_SUBSETS_ITEMS[attr] = value

ALL_POSSIBLE_SUBSETS = getAllPossibleSubsets(DATA, ALL_POSSIBLE_SUBSETS_ITEMS)

# Find information entropy for every found subset
attributesInfoGainRes = getInformationEntropyPerSubset(ALL_POSSIBLE_SUBSETS, DECISION_CLASSES_INFO_GAIN)

# Generate tree
returned = extractTreeData(attributesInfoGainRes)


def ID3(data, returnedValue):
    newSubsetItems = {list(returnedValue)[0]: {}}
    breakpointTrigger = False

    for item in returnedValue[list(returnedValue)[0]]:
        for key, val in ALL_POSSIBLE_ATTRIBUTES.items():
            if list(returnedValue)[0] == key:
                newSubsetItems[list(returnedValue)[0]][item] = ALL_POSSIBLE_ATTRIBUTES[key][item]

    updatedData = []
    for rec in data:
        for key, val in newSubsetItems.items():
            if rec[key] == val[list(val)[0]]:
                updatedData.append(rec)

    updatedRecordsPerDecisionAttribute = {}
    updatedQuantityOfRecordsPerDecisionAttribute = []
    for rec in updatedData:
        if updatedRecordsPerDecisionAttribute.get(rec[KEY_ATTRIBUTE]) is None:
            updatedRecordsPerDecisionAttribute[rec[KEY_ATTRIBUTE]] = 1
        else:
            updatedRecordsPerDecisionAttribute[rec[KEY_ATTRIBUTE]] += 1

    for key, val in updatedRecordsPerDecisionAttribute.items():
        updatedQuantityOfRecordsPerDecisionAttribute.append(val)
    t = information(updatedQuantityOfRecordsPerDecisionAttribute)

    updatedPossibleSubsets = getAllPossibleSubsets(updatedData, ALL_POSSIBLE_SUBSETS_ITEMS, list(returnedValue)[0])

    attributesInfoGainResult = getInformationEntropyPerSubset(updatedPossibleSubsets, t)

    returnedData = extractTreeData(attributesInfoGainResult)
    for key, val in returnedData.items():
        if len(val) == 0:
            breakpointTrigger = True
    if not breakpointTrigger:
        return ID3(updatedData, returnedData)


# Recursive call
ID3(DATA, returned)

# Print tree
printTree()
