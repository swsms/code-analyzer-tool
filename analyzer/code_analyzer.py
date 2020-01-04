code = input()
code_lines = code.split(sep='\\n')

for (num, line) in enumerate(code_lines, 1):
    if len(line) > 79:
        print(f'Line {num}: S001 Too long line')
