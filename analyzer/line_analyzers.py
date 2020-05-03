import re
from typing import List, Optional

from analyzer.contants import (CLASS_DECLARATION_REGEX, COMMENT_SIGN, FUN_DECLARATION_REGEX, INDENTATION_CODE,
                               INDENTATION_MSG, MAX_LINE_LENGTH, TODO_CODE, TODO_CODE_MSG, TOO_LONG_CODE,
                               TOO_LONG_LINE_MSG, TOO_MANY_BLANK_LINES_CODE, TOO_MANY_BLANK_LINES_MSG,
                               TOO_MANY_SPACES_CODE, TOO_MANY_SPACES_MSG_TEMPLATE, TWO_SPACES_BEFORE_COMMENT_CODE,
                               TWO_SPACES_BEFORE_COMMENT_MSG, UNNECESSARY_SEMICOLON_CODE, UNNECESSARY_SEMICOLON_MSG)
from analyzer.file_utils import (SourceCodeFile)
from analyzer.violation import Violation


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


def find_positions_with_too_many_blank_lines(lines: List[str]) -> List[int]:
    indexes = []
    for index in range(2, len(lines)):
        if (not check_lines_empty([lines[index]])
                and check_lines_empty(lines[index - 3: index])):
            indexes.append(index + 1)
    return indexes


def check_line_is_too_long(line: str) -> bool:
    return len(line) > MAX_LINE_LENGTH


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


def check_lines_empty(lines: List[str]) -> bool:
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
