import ast
import astpretty
source="""
def functionsample(a,b):
    c = a
    d = b
    return c,d
"""
node_structure = ast.parse(source)
print(node_structure)
astpretty.pprint(node_structure)
