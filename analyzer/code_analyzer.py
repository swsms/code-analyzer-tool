from typing import List, Tuple

TOO_LONG_CODE = 'S001'
TOO_LONG_LINE_MSG = 'Too long line'

INDENTATION_CODE = 'S002'
INDENTATION_MSG = 'Indentation is not a multiple of four'

TOO_MANY_BLANK_LINES_CODE = 'S003'
TOO_MANY_BLANK_LINES_MSG = 'Too many blank lines'

UNNECESSARY_SEMICOLON_CODE = 'S011'
UNNECESSARY_SEMICOLON_MSG = 'The line ends with an unnecessary semicolon'

TODO_CODE = 'S0012'
TODO_CODE_MSG = 'TODO found'

#

#
# NON ASCII CHARACTER (COLUMN?)
#
# check 4 TOO MANY BLANK LINES (3)


def read_code_lines(file_path: str) -> List[str]:
    with open(file_path, mode='r') as file:
        return [line.strip() for line in file.readlines()]


def analyze_code_lines(lines: List[str]) -> List[Tuple[int, str, str]]:
    violations = []

    for (num, line) in enumerate(lines, 1):
        if check_line_is_too_long(line):
            violations.append((num, TOO_LONG_CODE, TOO_LONG_LINE_MSG))

        if check_indentation_is_not_multiple_of_four(line):
            violations.append((num, INDENTATION_CODE, INDENTATION_MSG))

        if has_unnecessary_semicolon(line):
            violations.append((num, UNNECESSARY_SEMICOLON_CODE,
                               UNNECESSARY_SEMICOLON_MSG))

        if find_todo_within_comment(line):
            violations.append((num, TODO_CODE, TODO_CODE_MSG))

    positions = find_positions_with_too_many_blank_lines(lines)
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
            indexes.append(index)
    return indexes


def check_lines_empty(lines: List[str]):
    if not lines:
        return False
    return all([not line.strip() for line in lines])


def find_all_non_ascii_chars(line: str) -> List[Tuple[int, str]]:
    return [(index, str(char))
            for index, char in enumerate(line, 1)
            if not char.isascii()]


def has_unnecessary_semicolon(line: str) -> bool:
    return line.endswith(';')


def find_todo_within_comment(line: str) -> bool:
    todo_index = line.lower().find('todo')
    comment_sign_index = line.find('#')
    return todo_index >= 0 and 0 <= comment_sign_index < todo_index


def print_violations(violations: List[Tuple[int, str, str]]) -> None:
    for violation in violations:
        print(f'Line {violation[0]}: {violation[1]} {violation[2]}')


if __name__ == '__main__':
    file_path = input()
    code_lines = read_code_lines(file_path)
    violations = analyze_code_lines(code_lines)
    print_violations(violations)




