import ast
import re
from typing import List

import astpretty

from analyzer.contants import (
    CLASS_NAME_CODE, CLASS_NAME_MSG_TEMPLATE, CLASS_NAME_REGEX, FUN_ARG_NAME_CODE,
    FUN_ARG_NAME_MSG_TEMPLATE, FUN_ARG_VAR_NAME_REGEX, FUN_NAME_CODE, FUN_NAME_MSG_TEMPLATE,
    FUN_NAME_REGEX, FUN_VARIABLE_NAME_CODE, FUN_VARIABLE_NAME_TEMPLATE,
    MUTABLE_DEFAULT_ARGUMENT_CODE, MUTABLE_DEFAULT_NAME_TEMPLATE)
from analyzer.violation import Violation


# At this stage, we are going to check variable names using the AST module.
# You can rewrite some of the checks added in the previous stages using this approach.
# It would be especially convenient for checking the names of functions and classes.

def analyze_script_using_ast(file_path: str) -> List[Violation]:
    with open(file_path) as script:
        script_content = script.read()
        tree = ast.parse(script_content)
        # astpretty.pprint(tree)
        return find_violations_in_ast_tree(tree, file_path)


def find_violations_in_ast_tree(tree: ast.AST, file_path: str) -> List[Violation]:
    violations = []
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node
        violations += check_node(node, file_path)
    return violations


# TODO rewrite it using polymorphism
def check_node(node: ast.AST, file_path: str) -> List[Violation]:
    if isinstance(node, ast.FunctionDef):
        fun_name = node.name
        if not re.match(FUN_NAME_REGEX, fun_name):
            return [Violation(file_path=file_path, line=node.lineno,
                              code=FUN_NAME_CODE,
                              text=FUN_NAME_MSG_TEMPLATE % node.name)]
    if isinstance(node, ast.ClassDef):
        class_name = node.name
        violations = []
        if not re.match(CLASS_NAME_REGEX, class_name):
            violations.append(
                Violation(file_path=file_path, line=node.lineno,
                          code=CLASS_NAME_CODE,
                          text=CLASS_NAME_MSG_TEMPLATE % node.name)
            )
        return violations
    if isinstance(node, ast.arguments):
        violations = []
        args = node.args
        astpretty.pprint(node)
        for arg in args:
            if not re.match(FUN_ARG_VAR_NAME_REGEX, arg.arg):
                violations.append(
                    Violation(file_path=file_path, line=arg.lineno,
                              code=FUN_ARG_NAME_CODE,
                              text=FUN_ARG_NAME_MSG_TEMPLATE % arg.arg)
                )
        if node.defaults:
            mutable_defaults = {ast.List, ast.Dict, ast.Set}
            for default in node.defaults:
                for mutable_default in mutable_defaults:
                    if isinstance(default, mutable_default):
                        violations.append(
                            Violation(file_path=file_path, line=default.lineno,
                                      code=MUTABLE_DEFAULT_ARGUMENT_CODE,
                                      text=MUTABLE_DEFAULT_NAME_TEMPLATE)
                        )
                        break
        return violations
    if isinstance(node, ast.Assign):
        if isinstance(node.parent, ast.FunctionDef):
            fields = node.targets[0]
            if hasattr(fields, 'id'):
                variable_name = node.targets[0].id
                if not re.match(FUN_ARG_VAR_NAME_REGEX, variable_name):
                    return [Violation(file_path=file_path, line=node.lineno,
                                      code=FUN_VARIABLE_NAME_CODE,
                                      text=FUN_VARIABLE_NAME_TEMPLATE % variable_name)]
    return []
