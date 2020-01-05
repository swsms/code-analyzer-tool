from analyzer.code_analyzer import (
    check_line_is_too_long, check_indentation_is_not_multiple_of_four
)


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
