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

Prerequisites: variables, print, input, conditions, loops (for or for + while), split, enumerate(?) 

At the first stage, your program should read python code from the standard input 
and perform only a single check: lines in the source code must not be longer than 79 characters (PEP8!).

The lines of input source code are separated by \n. We assume, the extra \n are not used in the code (e.g, within strings).
It's just a simplification to get started. But empty code lines are suitable and should be considered. 

Here is an example:
```
print('What\'s your name?')
name = input()
print(f'Hello, {name}')  # here is an obvious comment: this prints greeting with a name

very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)
```

This code contains two long lines (> 79 characters): №3 and №5. Line numbers start with one.

It will be passed to the standard input in the following format with `\n` as line separators:
```
print('What\'s your name?')\nname = input()\nprint(f'Hello, {name}')  # here is an obvious comment: this prints greeting with a name\n\nvery_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000\nprint(very_big_number)
```

The general output format should be:
```
Line X: CODE Message 
```
Where 
- `X` is the number of a line where the issue found;
- `CODE` is an internal code of the stylistic issue;
- `Message` is a human-readable description for the issue.

This format will be used throughout the project.

Your program should find two style issues in this code and output them in the following format:
```
Line 3: S001 Too long line
Line 5: S001 Too long line
```
You can use another message instead of `Too long line`, but everything else should exactly match the example.
In our code `S001`, `S` means a stylistic issue, and `001` is the internal number of the issue.
