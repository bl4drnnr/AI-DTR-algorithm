from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute
from common import informationGain

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

CLASSES_INFO_GAIN = informationGain(quantityOfRecordsPerDecisionAttribute)

# Divide input data on subsets by attributes
print(ALL_POSSIBLE_ATTRIBUTES)
print()
for record in DATA:
    print(record)
# for attr, value in ALL_POSSIBLE_ATTRIBUTES.items():
#     if attr != KEY_ATTRIBUTE:
#         for records in DATA:

