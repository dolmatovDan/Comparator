import ast
import pprint
with open('main (4).py') as f:
    code = f.read()
print(code)
node = ast.parse(code)
# pprint.pprint(node.body[0]._fields)
pprint.pprint(ast.unparse(node.body[0]))