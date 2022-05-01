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

###################################################################
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

# TODO Update DATA [X] and start new iteration []
###################################################################

newSubsetItems = {list(returned)[0]: {}}

for item in returned[list(returned)[0]]:
    for attr, value in ALL_POSSIBLE_ATTRIBUTES.items():
        if list(returned)[0] == attr:
            newSubsetItems[list(returned)[0]][item] = ALL_POSSIBLE_ATTRIBUTES[attr][item]

updatedData = []
for record in DATA:
    for attr, value in newSubsetItems.items():
        if record[attr] == value[list(value)[0]]:
            updatedData.append(record)

updatedPossibleSubsets = getAllPossibleSubsets(updatedData, ALL_POSSIBLE_SUBSETS_ITEMS)
del updatedPossibleSubsets[list(returned)[0]]

test = getInformationEntropyPerSubset(updatedPossibleSubsets, DECISION_CLASSES_INFO_GAIN)
t = extractTreeData(test)
###################################################################


def ID3():
    return


# Print tree
printTree()
