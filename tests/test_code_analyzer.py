from analyzer.code_analyzer import *


def test_check_line_is_too_long():
    line = "print('hello')"
    assert not check_line_is_too_long(line)

    line = ("print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')")
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
    # assert not has_todo_comment("print(' # TODO')") TODO it does not work now


def test_check_lines_empty():
    assert not check_lines_empty([])
    assert check_lines_empty([' ', ' ', '  '])
    assert check_lines_empty([''])


def test_is_inside_singleline_string():
    assert not is_inside_singleline_string("12345", 3)
    assert not is_inside_singleline_string("12345", 10)
    assert not is_inside_singleline_string("12345", 0)
    assert not is_inside_singleline_string("print(12345)", 10)

    assert is_inside_singleline_string("print('12345')", 10)
    a = '12313\'sdfdsf\''
    assert is_inside_singleline_string("print('\'12\'', 3, '45')", 12)


def test_check_enough_spaces_before_comment():
    assert not check_lack_of_spaces_before_comment("# just a comment")
    assert not check_lack_of_spaces_before_comment("  # just a comment")
    assert not check_lack_of_spaces_before_comment("print('hello!')")
    assert not check_lack_of_spaces_before_comment("print('hello!')  #")
    assert not check_lack_of_spaces_before_comment("print('hello!')  # hello")

    assert check_lack_of_spaces_before_comment("print('hello!') # hello")
    assert check_lack_of_spaces_before_comment("print('hello!')# hello")


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
