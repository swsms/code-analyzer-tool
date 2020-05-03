import re
from os import path
from typing import List, Optional

from analyzer.ast_analyzer import analyze_script_using_ast
from analyzer.contants import (
    CLASS_DECLARATION_REGEX, CLASS_NAME_REGEX, COMMENT_SIGN,
    FUN_DECLARATION_REGEX, FUN_NAME_REGEX, INDENTATION_CODE, INDENTATION_MSG,
    TODO_CODE, TODO_CODE_MSG, TOO_LONG_CODE, TOO_LONG_LINE_MSG,
    TOO_MANY_BLANK_LINES_CODE, TOO_MANY_BLANK_LINES_MSG,
    TOO_MANY_SPACES_CODE, TOO_MANY_SPACES_MSG_TEMPLATE, TWO_SPACES_BEFORE_COMMENT_CODE,
    TWO_SPACES_BEFORE_COMMENT_MSG, UNNECESSARY_SEMICOLON_CODE, UNNECESSARY_SEMICOLON_MSG
)
from analyzer.file_utils import (get_file_names, read_file, read_python_files, SourceCodeFile)
from analyzer.violation import Violation


# TODO rewrite it using polymorphism
def analyze_code_lines(file: SourceCodeFile) -> List[Violation]:
    violations = []

    path = file[0]
    lines = file[1]
    for (num, line) in enumerate(lines, 1):
        if check_line_is_too_long(line):
            violations.append(
                Violation(file_path=path, line=num,
                          code=TOO_LONG_CODE,
                          text=TOO_LONG_LINE_MSG))

        if check_indentation_is_not_multiple_of_four(line):
            violations.append(
                Violation(file_path=path, line=num,
                          code=INDENTATION_CODE,
                          text=INDENTATION_MSG))

        if has_unnecessary_semicolon(line):
            violations.append(
                Violation(file_path=path, line=num,
                          code=UNNECESSARY_SEMICOLON_CODE,
                          text=UNNECESSARY_SEMICOLON_MSG))

        if check_lack_of_spaces_before_comment(line):
            violations.append(
                Violation(file_path=path, line=num,
                          code=TWO_SPACES_BEFORE_COMMENT_CODE,
                          text=TWO_SPACES_BEFORE_COMMENT_MSG))

        if has_todo_comment(line):
            violations.append(
                Violation(file_path=path, line=num,
                          code=TODO_CODE, text=TODO_CODE_MSG))

        construction = check_extra_space(line)
        if construction:
            violations.append(
                Violation(file_path=path, line=num,
                          code=TOO_MANY_SPACES_CODE,
                          text=TOO_MANY_SPACES_MSG_TEMPLATE % construction))

    violations.extend([
        Violation(file_path=path, line=position,
                  code=TOO_MANY_BLANK_LINES_CODE,
                  text=TOO_MANY_BLANK_LINES_MSG)
        for position in find_positions_with_too_many_blank_lines(lines)
    ])

    return violations


def check_line_is_too_long(line: str) -> bool:
    return len(line) > 79


def check_indentation_is_not_multiple_of_four(line: str) -> bool:
    spaces_count = 0
    char_number = 0
    while char_number < len(line):
        if line[char_number] == ' ':
            spaces_count += 1
        else:
            break
        char_number += 1
    return char_number % 4 != 0


def find_positions_with_too_many_blank_lines(lines: List[str]) -> List[int]:
    indexes = []
    for index in range(2, len(lines)):
        if (not check_lines_empty([lines[index]])
                and check_lines_empty(lines[index - 3: index])):
            indexes.append(index + 1)
    return indexes


def check_lines_empty(lines: List[str]):
    if not lines:
        return False
    return all([not line.strip() for line in lines])


def has_unnecessary_semicolon(line: str) -> bool:
    line = line.strip()

    last_semicolon_index = line.rfind(';')
    if last_semicolon_index < 0:
        return False

    first_comment_sign_index = line.find(COMMENT_SIGN)
    if last_semicolon_index == len(line) - 1:
        if 0 <= first_comment_sign_index < last_semicolon_index:
            return False
        return True

    index = last_semicolon_index + 1
    while index < len(line):
        if line[index] == '#':
            return True
        index += 1

    return False


def check_lack_of_spaces_before_comment(line: str) -> bool:
    first_comment_sign_index = line.find(COMMENT_SIGN)
    if first_comment_sign_index < 2:
        return False

    prev_index = first_comment_sign_index - 1
    preprev_index = first_comment_sign_index - 2

    return line[preprev_index] != ' ' or line[prev_index] != ' '


def has_todo_comment(line: str) -> bool:
    todo_index = line.lower().find('todo')
    comment_sign_index = line.find(COMMENT_SIGN)
    return todo_index >= 0 and 0 <= comment_sign_index < todo_index


def is_inside_singleline_string(line: str, target_index: int) -> bool:
    if target_index >= len(line):
        return False

    current_index = 1
    inside_single_quotes = False
    inside_double_quotes = False

    while current_index < target_index:
        if line[current_index - 1] == '\\':
            continue
        if line[current_index] == '\'':
            inside_single_quotes = not inside_double_quotes
        elif line[current_index] == '"':
            inside_double_quotes = not inside_double_quotes
        current_index += 1

    return inside_single_quotes or inside_double_quotes


def check_extra_space(line: str) -> Optional[str]:
    class_match_obj = re.match(CLASS_DECLARATION_REGEX, line.strip())
    if class_match_obj:
        numbers_of_spaces = len(class_match_obj.group(1))
        if numbers_of_spaces > 1:
            return 'class'

    fun_match_obj = re.match(FUN_DECLARATION_REGEX, line.strip())
    if fun_match_obj:
        numbers_of_spaces = len(fun_match_obj.group(1))
        if numbers_of_spaces > 1:
            return 'def'

    return None


def check_invalid_class_name(line: str) -> Optional[str]:
    class_match_obj = re.match(CLASS_DECLARATION_REGEX, line.strip())
    if not class_match_obj:
        return None

    class_name = class_match_obj.group(2)
    if not re.match(CLASS_NAME_REGEX, class_name):
        return class_name


def check_invalid_fun_name(line: str) -> Optional[str]:
    fun_match_obj = re.match(FUN_DECLARATION_REGEX, line.strip())
    if not fun_match_obj:
        return None

    fun_name = fun_match_obj.group(2)
    if not re.match(FUN_NAME_REGEX, fun_name):
        return fun_name


def sort_violations(violations: List[Violation]) -> List[Violation]:
    return sorted(violations,
                  key=lambda violation: [violation.file_path,
                                         violation.line,
                                         violation.code])


def print_violations(violations: List[Violation]) -> None:
    for violation in violations:
        print(f'{violation.file_path}: Line {violation.line}: '
              f'{violation.code} {violation.text}')


def main():
    file_path = input()
    if not path.exists(file_path):
        print('ERROR: The path does not exist!')
        return

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

    violations = sort_violations(violations)

    print_violations(violations)


if __name__ == '__main__':
    main()
