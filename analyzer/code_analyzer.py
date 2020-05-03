import sys
from os import path
from typing import List

from analyzer.analyzers.analyze_lines import analyze_code_lines
from analyzer.analyzers.ast_analyzer import analyze_script_using_ast
from analyzer.file_utils import (get_file_names, read_file, read_python_files)
from analyzer.violation import Violation


def sort_violations(violations: List[Violation]) -> List[Violation]:
    return sorted(violations,
                  key=lambda violation: [violation.file_path,
                                         violation.line,
                                         violation.code])


def print_violations(violations: List[Violation]) -> None:
    for violation in violations:
        print(f'{violation.file_path}: Line {violation.line}: '
              f'{violation.code} {violation.text}')


def analyze(file_path: str) -> List[Violation]:
    violations = []
    if path.isfile(file_path):
        source_code_files = [read_file(file_path)]
        violations.extend(analyze_script_using_ast(file_path))
    else:
        paths = get_file_names(file_path)
        for file_path in paths:
            violations.extend(analyze_script_using_ast(file_path))
        source_code_files = read_python_files(paths)

    for file in source_code_files:
        violations.extend(analyze_code_lines(file))

    return sort_violations(violations)


def main():
    file_path = input()
    if not path.exists(file_path):
        print('ERROR: The path does not exist!')
        return 1

    print_violations(analyze(file_path))


if __name__ == '__main__':
    sys.exit(main())
