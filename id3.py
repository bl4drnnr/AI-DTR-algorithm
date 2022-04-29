from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes

DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
INPUT_DATA_LENGTH = len(DATA)
GENERATED_TREE = []
