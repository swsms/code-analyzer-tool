from typing import List

from analyzer.analyzers.contants import (
    DEFAULT_CODE, TOO_MANY_BLANK_LINES_CODE, TOO_MANY_BLANK_LINES_MSG
)
from analyzer.analyzers.line_analyzers import (
    check_extra_space, check_indentation_is_not_multiple_of_four,
    check_lack_of_spaces_before_comment, check_line_is_too_long,
    find_positions_with_too_many_blank_lines, has_todo_comment,
    has_unnecessary_semicolon
)
from analyzer.file_utils import SourceCodeFile
from analyzer.violation import Violation

LINE_ANALYZERS = [
    check_line_is_too_long,
    check_indentation_is_not_multiple_of_four,
    has_unnecessary_semicolon,
    check_lack_of_spaces_before_comment,
    has_todo_comment,
    check_extra_space
]


def analyze_code_lines(file: SourceCodeFile) -> List[Violation]:
    violations = []

    path = file[0]
    lines = file[1]
    for (num, line) in enumerate(lines, 1):
        for line_analyzer in LINE_ANALYZERS:
            code, msg = line_analyzer(line)
            if code != DEFAULT_CODE:
                violations.append(Violation(file_path=path, line=num,
                                            code=code, text=msg))
    violations.extend([
        Violation(file_path=path, line=position,
                  code=TOO_MANY_BLANK_LINES_CODE,
                  text=TOO_MANY_BLANK_LINES_MSG)
        for position in find_positions_with_too_many_blank_lines(lines)
    ])

    return violations
