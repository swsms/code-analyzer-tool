import os
from typing import List, Tuple

SourceCodeFile = Tuple[str, List[str]]


def read_python_files(directory: str) -> List[SourceCodeFile]:
    paths = []

    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                paths.append(os.path.join('..', path, filename))

    return [read_file(path) for path in paths]


def read_file(file_path: str) -> SourceCodeFile:
    with open(file_path, mode='r') as file:
        return (file_path,
                [line.rstrip() for line in file.readlines()])

