import sys

InputCO = sys.argv[1]

if InputCO == '>':
    ComparisonOperator = 'GreaterThanThreshold'
    print(ComparisonOperator)
elif InputCO == '<':
    ComparisonOperator = 'LessThanThreshold'
    print(ComparisonOperator)
else:
    print('input Error!!!')

