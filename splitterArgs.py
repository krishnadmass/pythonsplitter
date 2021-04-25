import json
from splitter import splitbyArray
import sys
import ast

# data = json.loads(sys.argv[1])
d = ast.literal_eval(sys.argv[1])
print(d, type(d))
print(sys.argv[2])
splitbyArray(d, int(sys.argv[2]))
# try this to get a correct output
# python3 splitterArgs.py "[['a','b'],['c','d']]" 2