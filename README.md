# code-analyzer-tool
This is just a draft for a new project on Hyperskill.

Please, do not use it in production. A better choice would be pylint, flake8 or something else.

## Motivation

We really love python, and we also love to write beautiful and expressive code using it. 
One way to achieve this is to follow the PEP8 specification and best practices recommended by the python community.
But, this is not always easy, especially for beginners.

Fortunately, there are special tools called linters which automatically verify that code matches all the standards 
and recommendations. Well-known examples of such tools are pylint and flake8.

In this project, you will create a small linter which finds some common stylistic issues in python code.
This will allow you to understand the general ideas of static code analysis and also better understand python itself.

## First stage description

Prerequisites: variables, print, input, conditions, loops (for or for + while), split, enumerate(?) 

At the first stage, your tool should read source code from the standard input and performs two checks:
- too long ling (> 79 characters)
- the line ends with an unnecessary semicolon

The implementation of this stage allows you to get acquainted with the project and to comprehend the output format.
