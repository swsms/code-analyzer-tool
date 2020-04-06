# code-analyzer-tool
This is just a draft for a new project on Hyperskill.

Please, do not use it in production. A better choice would be pylint, flake8 or something else.

## Motivation

We really love python, and we also love to write beautiful and expressive code using it. 
One way to achieve this is to follow the PEP8 specification and best practices recommended by the python community.
But, this is not always easy, especially for beginners.

Fortunately, there are special tools called linters which automatically verify that code matches all the standards 
and recommendations. Well-known examples of such tools are pylint and flake8. 
They analyze code and output all the found stylistic and some other issues.

In this project, you will create a small linter which finds some common stylistic issues in python code.
This will allow you to understand the general ideas of static code analysis and also better understand python itself.

## Third stage description

**Prerequisites**: oop, directories

As a rule, real projects contain lots of different files. 
At this stage you need to improve the tool to make possible analyzing all python files
within a specified directory, skipping files of other types.

All previously implemented checks should work correctly.

Here are two examples below.

1) If only a single file is specified as the input:

Input example:
```
/path/to/file/script.py
```

Found issues: 

```
/path/to/file/script.py: Line 1: S004 At least two spaces before inline comment required
/path/to/file/script.py: Line 2: S003 Unnecessary semicolon
/path/to/file/script.py: Line 3: S001 Too long line
/path/to/file/script.py: Line 3: S003 Unnecessary semicolon
/path/to/file/script.py: Line 6: S001 Too long line
/path/to/file/script.py: Line 11: S006 More than two blank lines used before this line
/path/to/file/script.py: Line 13: S003 Unnecessary semicolon
/path/to/file/script.py: Line 13: S004 At least two spaces before inline comment required
/path/to/file/script.py: Line 13: S005 TODO found
```

2) If the input path is a directory, the output should contain all python files from it.

Input example:
```
/path/to/project
```

Found issues: 

```
/path/to/project/__init__.py: Line 1: S001 Too long line
/path/to/project/sctipt1.py: Line 1: S004 At least two spaces before inline comment required
/path/to/project/sctipt1.py: Line 2: S003 Unnecessary semicolon
/path/to/project/sctipt2.py: Line 1: S004 At least two spaces before inline comment required
/path/to/project/sctipt2.py: Line 3: S001 Too long line
/path/to/project/somedir/script.py: Line 3: S001 Too long line
/path/to/project/test.py: Line 3: Line 13: S003 Unnecessary semicolon
```

All output lines must be sorted according to the file name (lexicographically), line number and issue code.

As before, If a line contains the same stylistic issue several times (e.g., `[S003]`, `[S005]`), 
your program must print the information only once. But if a line has issues with different codes, 
they should be printed in the sorted order.

The path to a file with python code is obtained from the standard input as before.

It is highly recommended that you break down your program code into a set of small functions.
Otherwise, your code may confuse others.

To simplify the solution, we consider it acceptable if your program finds some false-positive stylistic issues 
within strings, especially multi-lines ('''...''' and """...""").
