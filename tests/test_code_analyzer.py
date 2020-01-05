import subprocess

PATH_TO_SCRIPT = 'analyzer/code_analyzer.py'
PATH_TO_SAMPLES_DIR = 'tests/samples'
ENCODING = 'utf-8'


def run_script_with_stdin(stdin_as_string) -> str:
    process = subprocess.Popen(['python', PATH_TO_SCRIPT],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)
    stdout = process.communicate(input=stdin_as_string.encode(ENCODING))[0]
    return stdout.decode(ENCODING)


def test_code_analyzer_when_single_line_without_issues():
    result = run_script_with_stdin(f'{PATH_TO_SAMPLES_DIR}/single_line_valid_example.py')
    assert not result


def test_code_analyzer_when_too_long_single_line():
    result = run_script_with_stdin(f'{PATH_TO_SAMPLES_DIR}/single_long_line_example.py')
    issues = result.splitlines()
    assert len(issues) == 1
    assert issues[0].startswith('Line 1: S001')


def test_when_multiple_long_lines():
    result = run_script_with_stdin(f'{PATH_TO_SAMPLES_DIR}/multiple_long_lines.py')
    issues = result.splitlines()
    assert len(issues) == 2
    assert issues[0].startswith('Line 3: S001')
    assert issues[1].startswith('Line 5: S001')
