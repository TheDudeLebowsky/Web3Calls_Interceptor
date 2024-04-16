import ast
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.')))
RESET = '\033[0m'
BOLDCYAN = '\033[1;36m'
BOLDBLUE = '\033[1;34m'
BOLD = '\033[1m'

"""Extracts variables from a Python file and returns their values as a dictionary where the key is the variable name and the value is the variable value."""



class VariableVisitor(ast.NodeVisitor):
    def __init__(self):
        self.variables = []
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variables.append(target.id)
        self.generic_visit(node)
    
    def visit_AugAssign(self, node):
        if isinstance(node.target, ast.Name):
            self.variables.append(node.target.id)
        self.generic_visit(node)
    


class FileExtractor():
    def __init__(self, filename = 'config/abi_list.py', debugmode = False):
        self.filename = filename
        self.debugmode = debugmode


    def find_variables_in_file(self):
        filename = self.filename
        """Extracts a list of variable names from a given Python file."""
        with open(filename, 'r', encoding='utf-8') as file:
            self.node = node = ast.parse(file.read(), filename=filename)
        self.variablevisitor = variablevisitor = VariableVisitor()
        variablevisitor.visit(node)
        self.variables_list = variablevisitor.variables
        return self.variables_list


    def get_variables_values(self, exclude_vars='DEFAULT_ABI_LIST'):

        if not hasattr(self, 'variables_list'):
            self.find_variables_in_file()

        if exclude_vars is None:
            exclude_vars = []

        local_vars = {}
        try:
            # Execute the code safely within a limited scope
            exec(open(self.filename).read(), {}, local_vars)
        except Exception as e:
            print(f"Error executing the code: {e}")
            return {}

        # Collect values of variables found, excluding specified variables
        variable_values = {var: local_vars.get(var)
                        for var in self.variables_list
                        if var not in exclude_vars}
        for key, value in variable_values.items():
            print(f"{BOLD}{key}{RESET} :  {BOLDCYAN}{value}{RESET}") if self.debugmode else None
        return variable_values

    

def main():
    fileextractor = FileExtractor(filename = 'config/abi_list.py', debugmode=True)
    fileextractor.get_variables_values()

if __name__ == "__main__":
    main()

