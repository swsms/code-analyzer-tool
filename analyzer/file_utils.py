import os
from typing import List, Tuple

SourceCodeFile = Tuple[str, List[str]]


def get_file_names(directory: str) -> List[str]:
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                paths.append(os.path.join('..', path, filename))
    return paths


def read_python_files(paths: List[str]) -> List[SourceCodeFile]:
    return [read_file(path) for path in paths]


def read_file(file_path: str) -> SourceCodeFile:
    with open(file_path, mode='r') as file:
        return (file_path,
                [line.rstrip() for line in file.readlines()])
