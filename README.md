# code-analyzer-tool
This is just a draft for a new project on Hyperskill.

Please, do not use it in production. A better choice would be pylint, flake8 or something else.

## Motivation

We really love python, and we also love to write beautiful and expressive code using it. 
One way to achieve this is to follow the PEP8 specification and best practices recommended by the python community. 
But, this is not always easy, especially for beginners. 
Fortunately, there are special tools called static code analyzers (pylint, flake8, etc) which can automatically verify 
that your code matches all the standards and recommendations. 
The tools analyze your code and output all the found stylistic and other issues.

In this project, you will create a small static analyzer tool which finds a set of common stylistic issues in python code. 
It allows you to understand general ideas of the static code analysis and deepen your python knowledge as well.

## Third stage description

**Prerequisites**: oop, directories

As a rule, real projects contain more than a single file. 
At this stage you need to improve your program to make possible analyzing all python files inside a specified directory.
Other files must be skipped.

You also need to change the input format. Now, instead of reading the path from the standard input,
it must be obtained as a command line argument.

```
> python code_analyzer.py directory-or-file
```

It is important, that all the checks implemented on the previous stages should work correctly.

Here are three examples below.

1) If only a single file is specified as the input:

```
> python code_analyzer.py /path/to/file/script.py
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

2) If the input path is a directory, the output should contain all python files from it:

```
> python code_analyzer.py /path/to/project
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
