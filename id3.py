from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute

DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
INPUT_DATA_LENGTH = len(DATA)
GENERATED_TREE = []

# Find information entropy for decision attribute
quantityOfRecordsPerDecisionAttribute = {}
for record in DATA:
    if quantityOfRecordsPerDecisionAttribute.get(record[KEY_ATTRIBUTE]) is None:
        quantityOfRecordsPerDecisionAttribute[record[KEY_ATTRIBUTE]] = 1
    else:
        quantityOfRecordsPerDecisionAttribute[record[KEY_ATTRIBUTE]] += 1
