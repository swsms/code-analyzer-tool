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

## First stage description

**Prerequisites**: variables, print, input, conditions, for, split, enumerate(?), reading files

At this moment, your program must read python code from a specified file and perform only a single check: 
lines in the code must not be longer than 79 characters (PEP8!). 
The path to a file is obtained from the standard input.

Here are some examples for different operating systems.
- Linux or MacOS
```
/home/someuser/projects/hello_script.py
```
- Windows
```
C:\myprojects\hello_script.py
```

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

Here is an expected output for the given example:
```
Line 3: S001 Too long line
Line 5: S001 Too long line
```
The order must always be from the first to last line.

Your program can output another `message` instead of Too `long line`. 
The rest part of the output must exactly match the provided example. 
In this code S001, S means a stylistic issue, and `001` is the internal number of the issue.
