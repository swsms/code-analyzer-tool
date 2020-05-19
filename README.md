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

## Fourth stage description

**Prerequisites**: regexps

As many people say, naming things is one of the hardest problems in programming.
At the same time, good names make a program more readable and uniform.

At this stage, you need to improve your code analyzer to check 
names of all functions and classes in a given program according to PEP8.

You need to add the following three checks:
- `[S007]` Too many spaces after '%constuction_name%' (def or class)
- `[S008]` Class name '%class_name%' should use CamelCase
- `[S009]` Function name '%function_name%' should use snake_case

You can use other messages, but check codes must be exactly the same.
All previously implemented checks should work correctly.

To simplify the problem, we suppose that classes are always written like the following examples:

```
# a simple class
class MyClass:
    pass
    
# a class based on inheritance
class MyClass(AnotherClass):
    pass
```

In reality it's possible to declare a class in this way:

```
class \
        S:
    pass
```

But it is not a common way to declare classes and you can skip it.

Another assumption that functions are always declared like this one:

```
def do_magic():
    pass
```

Functions that starts and ends with underscores (`__fun`, `__init__`) must be admissible too.

Here is an input code example:

```
class  Person:
    pass

class user:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def _print1():
        print('q')

    @staticmethod
    def Print2():
        print('q')
```

The expected output for this code is the following:
```
/path/to/file/script.py: Line 1: S007 Too many spaces after 'class'
/path/to/file/script.py: Line 4: S008 Class name 'user' should use CamelCase
/path/to/file/script.py: Line 15: S009 Function name 'Print2' should use snake_case
```

It is as acceptable if your program finds some false-positive stylistic issues 
within strings, especially multi-lines ('''...''' and """..."""). 
But you can improve this case if you want.
