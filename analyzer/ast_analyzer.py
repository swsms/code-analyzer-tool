import ast
import re

import astpretty

from analyzer.code_analyzer import (
    CLASS_NAME_CODE, CLASS_NAME_MSG_TEMPLATE, FUN_ARG_NAME_CODE,
    FUN_ARG_NAME_MSG_TEMPLATE, FUN_NAME_CODE, FUN_NAME_MSG_TEMPLATE,
    FUN_VARIABLE_NAME_CODE, FUN_VARIABLE_NAME_TEMPLATE)
from analyzer.contants import FUN_NAME_REGEX, FUN_ARG_VAR_NAME_REGEX, CLASS_NAME_REGEX
from analyzer.violation import Violation

# At this stage, we are going to check variable names using the AST module.
# You can rewrite some of the checks added in the previous stages using this approach.
# It would be especially convenient for checking the names of functions and classes.

file_path = '/home/artyom/MyProjects/code-analyzer-tool/tests/samples/names_examples.py'
script = open('/home/artyom/MyProjects/code-analyzer-tool/tests/samples/names_examples.py')
script_content = script.read()
script.close()

tree = ast.parse(script_content)
# astpretty.pprint(tree)

children_to_parents_dict = dict()

violations = []

for node in ast.walk(tree):
    for child in ast.iter_child_nodes(node):
        child.parent = node
    if isinstance(node, ast.FunctionDef):
        fun_name = node.name
        if not re.match(FUN_NAME_REGEX, fun_name):
            violations.append(
                Violation(file_path=file_path, line=node.lineno,
                          code=FUN_NAME_CODE,
                          text=FUN_NAME_MSG_TEMPLATE % node.name)
            )
    if isinstance(node, ast.ClassDef):
        class_name = node.name
        if not re.match(CLASS_NAME_REGEX, class_name):
            violations.append(
                Violation(file_path=file_path, line=node.lineno,
                          code=CLASS_NAME_CODE,
                          text=CLASS_NAME_MSG_TEMPLATE % node.name)
            )
    if isinstance(node, ast.arguments):
        args = node.args
        for arg in args:
            if not re.match(FUN_ARG_VAR_NAME_REGEX, arg.arg):
                violations.append(
                    Violation(file_path=file_path, line=arg.lineno,
                              code=FUN_ARG_NAME_CODE,
                              text=FUN_ARG_NAME_MSG_TEMPLATE % arg.arg)
                )
    if isinstance(node, ast.Assign):
        if isinstance(node.parent, ast.Module):
            continue
        if isinstance(node.parent, ast.ClassDef):
            continue
        if isinstance(node.parent, ast.FunctionDef):
            variable_name = node.targets[0].id
            if not re.match(FUN_ARG_VAR_NAME_REGEX, variable_name):
                violations.append(
                    Violation(file_path=file_path, line=node.lineno,
                              code=FUN_VARIABLE_NAME_CODE,
                              text=FUN_VARIABLE_NAME_TEMPLATE % variable_name)
                )


for violation in violations:
    print(violation)


