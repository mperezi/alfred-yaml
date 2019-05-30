import yaml, sys
from io import BytesIO

CONTEXT=2

input = sys.stdin.read()

def format_error(line, column, error):
    yml = input.split("\n")

    prev = line-CONTEXT
    while prev < line:
        if prev > 0: 
            print("%s: %s" % (str(prev), yml[prev-1])) 
        prev += 1

    prefix = str(line) + ": "
    print(prefix + yml[line-1])
    print(" " * (len(prefix)+column-1) + "^")
    print(error)

try:
    yaml.safe_load(BytesIO(input))
    print("Valid YAML!")
except yaml.YAMLError as ex:
    mark = ex.problem_mark
    format_error(mark.line+1, mark.column+1, ex.problem)
