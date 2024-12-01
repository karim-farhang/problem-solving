import ast

# Creating AST
code = ast.parse("print('Welcome To PythonPool')")
print(code)
# Printing AST
print(ast.dump(code))
# Executing AST
exec(compile(code, filename="", mode="exec"))

# Creating AST
code = ast.parse("print([1,2,3,4,5])")
# Printing AST
print(ast.dump(code))
# Executing AST
exec(compile(code, filename="", mode="exec"))

# Creating AST
code = ast.parse("print(10+12)")
# Printing AST
print(ast.dump(code))
# Executing AST
exec(compile(code, filename="", mode="exec"))

tree_ast = ast.parse('''  
location = ['Agra', 'UP']  
name = 'Taj Mahal'  

print('{} is located in {},{}'.format(name, location[0],location[1]))  
''')

print(ast.dump(tree_ast))

exec(compile(tree_ast, filename="", mode="exec"))

# Creating AST
code = ast.parse("# This is a comment")
print(code)
# Printing AST
print(ast.dump(code))
# Executing AST
exec(compile(code, filename="", mode="exec"))


class EvaluateExpression(ast.NodeTransformer):
    # Defining operations for operators
    ops = {
        ast.Add: '+',
        ast.Sub: '-',
        ast.Mult: '*',
        ast.Div: '/',
    }

    def visit_BinOp(self, node):
        self.generic_visit(node)
        if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
            value = eval(f'{node.left.n} {self.ops[type(node.op)]} {node.right.n}')
            return ast.Num(n=value)
        return node


tree = ast.parse('3+2+7+8')
tree = ast.fix_missing_locations(EvaluateExpression().visit(tree))
print(ast.dump(tree))
