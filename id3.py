from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute
from common import extractTreeData, printTree, getAllPossibleSubsets, getInformationEntropyPerSubset, updateRecordsPerAttribute

DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
INPUT_DATA_LENGTH = len(DATA)

# Find information entropy for decision attribute
recordsPerDecisionAttribute = updateRecordsPerAttribute(DATA)

# Divide input data on subsets by attributes
ALL_POSSIBLE_SUBSETS_ITEMS = {}

for attr, value in ALL_POSSIBLE_ATTRIBUTES.items():
    if attr != KEY_ATTRIBUTE:
        ALL_POSSIBLE_SUBSETS_ITEMS[attr] = value

ALL_POSSIBLE_SUBSETS = getAllPossibleSubsets(DATA, ALL_POSSIBLE_SUBSETS_ITEMS)

# Find information entropy for every found subset
attributesInfoGainRes = getInformationEntropyPerSubset(ALL_POSSIBLE_SUBSETS, recordsPerDecisionAttribute)

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

    updateRecordsPerDecisionAttribute = updateRecordsPerAttribute(updatedData)

    updatedPossibleSubsets = getAllPossibleSubsets(updatedData, ALL_POSSIBLE_SUBSETS_ITEMS)

    attributesInfoGainResult = getInformationEntropyPerSubset(updatedPossibleSubsets, updateRecordsPerDecisionAttribute)

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
