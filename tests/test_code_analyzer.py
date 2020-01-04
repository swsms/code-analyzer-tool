import subprocess

PATH_TO_SCRIPT = 'analyzer/code_analyzer.py'
ENCODING = 'utf-8'


def run_script_with_stdin(stdin_as_string) -> str:
    process = subprocess.Popen(['python', PATH_TO_SCRIPT],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)
    stdout = process.communicate(input=stdin_as_string.encode(ENCODING))[0]
    return stdout.decode(ENCODING)


def test_code_analyzer_when_single_line_without_issues():
    result = run_script_with_stdin('./tests/samples/single_line_valid_example.py')
    assert not result


def test_code_analyzer_when_too_long_single_line():
    result = run_script_with_stdin('./tests/samples/single_long_line_example.py')
    issues = result.splitlines()
    assert len(issues) == 1
    assert issues[0].startswith('Line 1: S001')


test_code_analyzer_when_too_long_single_line()
#
# def test_code_analyzer_when_too_long_single_line():
#     code = "print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!')"
#     result = run_script_with_stdin(code)
#     issues = result.splitlines()
#     assert len(issues) == 1
#
#
# def test_code_analyzer_when_multiple_lines():
#     code = """print('What\'s your name?')
#     name = input()\n\n"
#            "print(f'Hello, {name}')  # here is an obvious comment: this prints greeting with a name\n\n"
#            "very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000\n"
#            "print(very_big_number)"""
#
#     result = run_script_with_stdin(code)
#     print(result)
#
#
# def pass_multiline_string():
#     sys.stdin = io.StringIO('print()\n\nprint()')
#     runpy.run_path(
#         '../analyzer/code_analyzer.py',
#     )
