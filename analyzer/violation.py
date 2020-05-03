from dataclasses import dataclass


@dataclass(frozen=True)
class Violation:
    file_path: str
    line: int
    code: str
    text: str = ''
