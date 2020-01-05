from analyzer.code_analyzer import *


def test_check_line_is_too_long():
    line = "print('hello')"
    assert not check_line_is_too_long(line)

    line = "print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')"
    assert check_line_is_too_long(line)


def test_check_indentation_is_not_multiple_of_four():
    line = "print('hello')"
    assert not check_indentation_is_not_multiple_of_four(line)

    line = " print('hello')"
    assert check_indentation_is_not_multiple_of_four(line)

    line = "  print('hello')"
    assert check_indentation_is_not_multiple_of_four(line)

    line = "    print('hello')"
    assert not check_indentation_is_not_multiple_of_four(line)

    line = "       print('hello')"
    assert check_indentation_is_not_multiple_of_four(line)

    line = "        print('hello')"
    assert not check_indentation_is_not_multiple_of_four(line)


def test_has_unnecessary_semicolon():
    assert not has_unnecessary_semicolon("print('hello')")
    assert has_unnecessary_semicolon("print('hello');")
    assert has_unnecessary_semicolon("print('hello');  ")
    assert has_unnecessary_semicolon("print('hello');;;")
    assert has_unnecessary_semicolon("print('hello');  # hello")
    assert not has_unnecessary_semicolon("# hello hello hello;")
    assert not has_unnecessary_semicolon("greeting = 'hello;'")
    assert not has_unnecessary_semicolon("'Hello; ;#; ;Hello;'")
    assert not has_unnecessary_semicolon("print('hello')  #;")


def test_has_todo_comment():
    assert not has_todo_comment("print('hello')")
    assert has_todo_comment("print('hello')  # TODO")
    assert has_todo_comment("print('hello')  # TODO # TODO")
    assert has_todo_comment("# todo")
    assert has_todo_comment("# TODO just do it")
    assert not has_todo_comment("print('todo')")
    assert not has_todo_comment("print('TODO TODO')")
    assert not has_todo_comment("todo()")
    assert not has_todo_comment("todo = 'todo'")


def test_find_positions_with_too_many_blank_lines():
    lines = [
        "print('hello')"
    ]

    assert [] == find_positions_with_too_many_blank_lines(lines)

    lines = [
        "",
        "",
        "print('hello')",
        "",
        "",
        "",
        "",
        "",
        "print('hello')"
    ]

    assert [8] == find_positions_with_too_many_blank_lines(lines)

    lines = [
        "print('hello')",
        "",
        "",
        "",
        "",
        "    print('hello')",
        "",
        "",
        "",
        "print('hello')",
        "",
        "",
        "print('hello')",
    ]

    assert [5, 9] == find_positions_with_too_many_blank_lines(lines)
