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

## First stage description

**Prerequisites**: declaring functions, slicing, list comprehensions, while, sorting

At this stage, you need to add five new checks in your program:
- `[S002]` Indentation is not a multiple of four 
- `[S003]` Unnecessary semicolon after a statement (note, semicolons are admissible in comments)
- `[S004]` At least two spaces before inline comment required
- `[S005]` TODO found (only within comments and the case does not important) 
- `[S006]` More than two blank lines used before this line (it must be output for the first non-empty line)

All of the checks are consistent with the PEP8 style guide. 
See an example below to better understand the checks.

If a line contains the same stylistic issue several times (e.g., `[S003]`, `[S005]`), 
your program must print the information only once. But if a line has issues with different codes, 
they should be printed in the sorted order.

The path to a file with python code is obtained from the standard input as before.

It is highly recommended that you break down your program code into a set of small functions.
Otherwise, your code may confuse others.

Here is an example of a file with bad code.
```
print('What\'s your name?') # reading an input
name = input();
print(f'Hello, {name}');  # here is an obvious comment: this prints greeting with a name


very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)



def some_fun():
    print('NO TODO HERE;;')
    pass; # Todo something
```

It contains 9 code style issues.

```
Line 1: S004 At least two spaces before inline comment required
Line 2: S003 Unnecessary semicolon
Line 3: S001 Too long line
Line 3: S003 Unnecessary semicolon
Line 6: S001 Too long line
Line 11: S006 More than two blank lines used before this line
Line 13: S003 Unnecessary semicolon
Line 13: S004 At least two spaces before inline comment required
Line 13: S005 TODO found
```

The order of stylistic issues must always be from the first to last line.

You can print another `message` instead of our examples (like `Too long line`), 
but everything else must exactly match the example.
In our code `S001`, `S` means a stylistic issue, and `001` is the internal number of the issue.

To simplify the solution, we consider it acceptable if your program will find some false-positive stylistic issues 
within strings, especially multi-lines ('''...''' and """...""").
