# code-analyzer-tool
This is just a draft for a new education project on Hyperskill. The published project may be slightly different, so there is no ready-made solution in this repository :)

**Please, do not use this tool in production. A better choice would be flake8, pylint or something else.**

## Motivation

We really love python, and we also love to write beautiful and expressive code using it. 
One way to achieve this is to follow the PEP8 specification and best practices recommended by the python community.
But, this is not always easy, especially for beginners.

Fortunately, there are special tools called linters which automatically verify that code matches all the standards 
and recommendations. Well-known examples of such tools are pylint and flake8. 
They analyze code and output all the found stylistic and some other issues.

In this project, you will create a small linter which finds some common stylistic issues in python code.
This will allow you to understand the general ideas of static code analysis and also better understand python itself.

## Fifth stage description

**Prerequisites**: ast, tree traversals

At this stage, you need to improve your code analyzer to check all names of function arguments 
and local variables according to PEP8. 
The program must not force the names of variables outside functions (e.g., in modules or classes).
The most convenient way to do this is to use the AST tree from the `ast` module.

Also, your program must analyze that the given code does not use mutable values (lists, dicts, sets) 
as default arguments to avoid errors in the program.

You need to add the following three checks:
- `[S010]` Argument name '%arg_name%' should be snake_case
- `[S011]` Variable '%var_name%' in function should be snake_case
- `[S012]` Default argument value is mutable

You can use other messages, but check codes must be exactly the same.
All previously implemented checks should work correctly as well as reading from one or more files.

To simplify the problem, you only need to check whether the mutable value is directly assigned to an argument.

```
def fun1(test=[]):  # default argument value is mutable
    pass


def fun2(test=get_value()):  # you can skip this case to simplify the problem
    pass
```

If a function contains several mutable arguments, the message must be output only once for this function.

Variable and argument names are assumed to be valid if they use snake_case. 
Initial underscores (_) are considered as admissible too.

Here is an input code example:

```python
CONSTANT = 10
names = ['John', 'Lora', 'Paul']


def fun1(S=5, test=[]):  # default argument value is mutable
    VARIABLE = 10
    string = 'string'
    print(VARIABLE)
```

The expected output for this code is the following:

```
/path/to/file/script.py: Line 5: S010 Argument name 'S' should be snake_case
/path/to/file/script.py: Line 5: S012 Default argument value is mutable
/path/to/file/script.py: Line 6: S011 Variable 'VARIABLE' in function should be snake_case
```

You can also use AST to rewrite some of the checks added before.
It would be especially convenient for checking the names of functions and classes.
