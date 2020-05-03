import re
from typing import Callable, List, Optional, Tuple

from analyzer.analyzers.contants import (
    CLASS_DECLARATION_REGEX, COMMENT_SIGN, DEFAULT_CODE, DEFAULT_MSG, FUN_DECLARATION_REGEX,
    INDENTATION_CODE, INDENTATION_MSG, MAX_LINE_LENGTH, TODO_CODE, TODO_CODE_MSG,
    TOO_LONG_CODE, TOO_LONG_LINE_MSG, TOO_MANY_SPACES_CODE, TOO_MANY_SPACES_MSG_TEMPLATE,
    TWO_SPACES_BEFORE_COMMENT_CODE, TWO_SPACES_BEFORE_COMMENT_MSG,
    UNNECESSARY_SEMICOLON_CODE, UNNECESSARY_SEMICOLON_MSG
)


def analyzer(code: str, message: str = '', template: str = '') -> Callable:
    def decorator(function: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Tuple[str, str]:
            result = function(*args, **kwargs)
            if not result:
                return DEFAULT_CODE, DEFAULT_MSG
            if message:
                return code, message
            if template:
                return code, template % result
        return wrapper
    return decorator


@analyzer(code=TOO_LONG_CODE, message=TOO_LONG_LINE_MSG)
def check_line_is_too_long(line: str) -> bool:
    return len(line) > MAX_LINE_LENGTH


@analyzer(code=INDENTATION_CODE, message=INDENTATION_MSG)
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


@analyzer(code=UNNECESSARY_SEMICOLON_CODE,
          message=UNNECESSARY_SEMICOLON_MSG)
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


def check_lines_empty(lines: List[str]) -> bool:
    if not lines:
        return False
    return all([not line.strip() for line in lines])


@analyzer(code=TWO_SPACES_BEFORE_COMMENT_CODE,
          message=TWO_SPACES_BEFORE_COMMENT_MSG)
def check_lack_of_spaces_before_comment(line: str) -> bool:
    first_comment_sign_index = line.find(COMMENT_SIGN)
    if first_comment_sign_index < 2:
        return False

    prev_index = first_comment_sign_index - 1
    preprev_index = first_comment_sign_index - 2

    return line[preprev_index] != ' ' or line[prev_index] != ' '


@analyzer(code=TODO_CODE, message=TODO_CODE_MSG)
def has_todo_comment(line: str) -> bool:
    todo_index = line.lower().find('todo')
    comment_sign_index = line.find(COMMENT_SIGN)
    return todo_index >= 0 and 0 <= comment_sign_index < todo_index


@analyzer(code=TOO_MANY_SPACES_CODE,
          template=TOO_MANY_SPACES_MSG_TEMPLATE)
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


def find_positions_with_too_many_blank_lines(lines: List[str]) -> List[int]:
    indexes = []
    for index in range(2, len(lines)):
        if (not check_lines_empty([lines[index]])
                and check_lines_empty(lines[index - 3: index])):
            indexes.append(index + 1)
    return indexes



