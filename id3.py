from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute
from common import informationGain, countItems

DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
INPUT_DATA_LENGTH = len(DATA)
GENERATED_TREE = []

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

DECISION_CLASSES_INFO_GAIN = informationGain(quantityOfRecordsPerDecisionAttribute)

# Divide input data on subsets by attributes
ALL_POSSIBLE_SUBSETS_ITEMS = {}
ALL_POSSIBLE_SUBSETS = {}

for attr, value in ALL_POSSIBLE_ATTRIBUTES.items():
    if attr != KEY_ATTRIBUTE:
        ALL_POSSIBLE_SUBSETS_ITEMS[attr] = value

for attr, value in ALL_POSSIBLE_SUBSETS_ITEMS.items():

    for record in DATA:
        for recAttr, recValue in record.items():
            if attr == recAttr:

                for attrSubset, valueSubset in value.items():
                    if recValue == valueSubset and ALL_POSSIBLE_SUBSETS.get(attr) is None:
                        ALL_POSSIBLE_SUBSETS[attr] = {}
                        ALL_POSSIBLE_SUBSETS[attr][attrSubset] = [record[KEY_ATTRIBUTE]]
                    elif recValue == valueSubset and ALL_POSSIBLE_SUBSETS.get(attr) is not None:
                        if ALL_POSSIBLE_SUBSETS[attr].get(attrSubset) is None:
                            ALL_POSSIBLE_SUBSETS[attr][attrSubset] = {}
                            ALL_POSSIBLE_SUBSETS[attr][attrSubset] = [record[KEY_ATTRIBUTE]]
                        else:
                            ALL_POSSIBLE_SUBSETS[attr][attrSubset].append(record[KEY_ATTRIBUTE])

# Find information entropy for every found subset
for attr, value in ALL_POSSIBLE_SUBSETS.items():
    attributeInfoGainItems = []
    attributeInfoGain = None
    for key, val in value.items():
        countSubsetInfo = countItems(val)
        extractedSubsetInfo = []
        for x, y in countSubsetInfo.items():
            extractedSubsetInfo.append(y)
        attributeInfoGainItems.append(informationGain(extractedSubsetInfo))
    print("Class:", attr)
    print("Information gain:", informationGain(attributeInfoGainItems))
    print('----------')
