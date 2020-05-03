COMMENT_SIGN = '#'

CLASS_DECLARATION_REGEX = r'class(\s+)(\w+):'
CLASS_NAME_REGEX = r'_?[A-Z][a-zA-Z0-9]*'

FUN_DECLARATION_REGEX = r'def(\s+)(\w+)'
FUN_NAME_REGEX = r'(_*[a-z0-9_])'

FUN_ARG_VAR_NAME_REGEX = r'(_*[a-z0-9_])'

MAX_LINE_LENGTH = 79

DEFAULT_CODE = 'OK'
DEFAULT_MSG = ''

TOO_LONG_CODE = 'S001'
TOO_LONG_LINE_MSG = 'Too long line'

INDENTATION_CODE = 'S002'
INDENTATION_MSG = 'Indentation is not a multiple of four'

UNNECESSARY_SEMICOLON_CODE = 'S003'
UNNECESSARY_SEMICOLON_MSG = 'Unnecessary semicolon'

TWO_SPACES_BEFORE_COMMENT_CODE = 'S004'
TWO_SPACES_BEFORE_COMMENT_MSG = ('At least two spaces before '
                                 'inline comment required')

TODO_CODE = 'S005'
TODO_CODE_MSG = 'TODO found'

TOO_MANY_BLANK_LINES_CODE = 'S006'
TOO_MANY_BLANK_LINES_MSG = 'More than two blank lines used before this line'

TOO_MANY_SPACES_CODE = 'S007'
TOO_MANY_SPACES_MSG_TEMPLATE = 'Too many spaces after \'%s\''

CLASS_NAME_CODE = 'S008'
CLASS_NAME_MSG_TEMPLATE = 'Class name \'%s\' should use CamelCase'

FUN_NAME_CODE = 'S009'
FUN_NAME_MSG_TEMPLATE = 'Function name \'%s\' should use snake_case'

FUN_ARG_NAME_CODE = 'S010'
FUN_ARG_NAME_MSG_TEMPLATE = 'Argument name \'%s\' should be snake_case'

FUN_VARIABLE_NAME_CODE = 'S011'
FUN_VARIABLE_NAME_TEMPLATE = 'Variable \'%s\' in function should be snake_case'

MUTABLE_DEFAULT_ARGUMENT_CODE = 'S012'
MUTABLE_DEFAULT_NAME_TEMPLATE = 'Default argument value is mutable'
