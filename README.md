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

**Prerequisites**: declaring functions, slicing, list comprehensions

At this stage, you need to add five new checks in your program:
- Indentation is not a multiple of four [S002]
- The line ends with an unnecessary semicolon [S003]
- At least two spaces before inline comment required [S004]
- TODO found [S005]
- More than two blank lines used [S006]

All of the checks are consistent with the PEP8 style guide.

The path to a file with python code is obtained from the standard input as before.

It is highly recommended that you break down your program code into a set of small functions.
Otherwise, your code may confuse others.

Here is an example of the file's content.
```
print('What\'s your name?')
name = input()
print(f'Hello, {name}')  # here is an obvious comment: this prints greeting with a name

very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)
```

This code contains two long lines (> 79 characters): №3 and №5.

The general output format is:
```
Line X: Code Message 
```
Where 
- `X` is the number of a line where the issue found, it starts with one;
- `Code` is the code of the stylistic issue (like `S001`);
- `Message` is a human-readable description for the issue (optional).

This format will be used throughout the project.

Your program should output the following style issues for the given example:
```
Line 3: S001 Too long line
Line 5: S001 Too long line
```
The order must always be from the first line to last one.

You can use another message instead of `Too long line`, but everything else should exactly match the example.
In our code `S001`, `S` means a stylistic issue, and `001` is the internal number of the issue.
